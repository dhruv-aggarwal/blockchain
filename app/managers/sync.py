import os
import json
from app.models.block import Block
from app.models.chain import Chain
from common import get_data_directory
from app import app
import requests
PEERS = app.config['PEERS']


def sync_local():
    node_blocks = []
    # Assuming that the folder and at least initial block exists
    data_dir = get_data_directory()
    if os.path.exists(data_dir):
        for filename in os.listdir(data_dir):
            # Check on the files that are stored in the required format.
            # No need to look in all the files
            if filename.endswith('.json'):
                filepath = '%s/%s' % (data_dir, filename)
            with open(filepath, 'r') as block_file:
                block_info = json.load(block_file)
                block_object = Block(**block_info)
                node_blocks.append(block_object)
    return node_blocks


def sync_overall(save=False):
    best_chain = Chain(sync_local())
    for peer in PEERS:
        # try to connect to peer
        peer_blockchain_url = peer + 'blockchain.json'
        try:
            r = requests.get(peer_blockchain_url)
            peer_blockchain_dict = r.json()
            peer_blocks = [
                Block(**bdict) for bdict in peer_blockchain_dict
            ]
            peer_chain = Chain(peer_blocks)

            if peer_chain.is_valid() and peer_chain > best_chain:
                best_chain = peer_chain

        except requests.exceptions.ConnectionError:
            print "Peer at %s not running. Continuing to next peer." % peer

    print "Longest blockchain is %s blocks" % len(best_chain)
    # for now, save the new blockchain over whatever was there
    if save:
        best_chain.save()
    return best_chain


def sync(save=False):
    return sync_overall(save=save)

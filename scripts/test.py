from app.models.block import Block
from datetime import datetime
import os
from app.managers.common import get_data_directory, calculate_hash
from app.managers.block import save_block


def initialize_block():
    # index zero and arbitrary previous hash
    block_data = {}
    block_data['index'] = 0
    block_data['timestamp'] = datetime.now()
    block_data['data'] = 'First block data'
    block_data['prev_hash'] = None
    block_data['hash'] = calculate_hash(
        0, None, block_data['data'], block_data['timestamp'], 0
    )
    block = Block(block_data)
    return block


def save_to_file():
    # blockchain_dir is the directory where the each block is stored locally
    # in the file system.
    # If the folder does not exist, need to create it.
    directory = get_data_directory()
    if not os.path.exists(directory):
        # make chaindata dir
        os.mkdir(directory)
    # if the folder is empty, initialise the blockchain. Else add to it.to
    # TODO: Add to an existing chain
    # TODO: Save block to a file
    if os.listdir(directory) == []:
        # create first block
        first_block = initialize_block()
        save_block(first_block)

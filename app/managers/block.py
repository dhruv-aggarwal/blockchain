from common import get_block_filename, calculate_hash
import json
from datetime import datetime
from app.models.block import Block


def save_block(block):
    filename = get_block_filename(block.index)
    with open(filename, 'w') as block_file:
        json.dump(block.__dict__(), block_file)


def mine(last_block):
    index = int(last_block.index) + 1
    timestamp = datetime.utcnow()
    # random string for now
    data = "I block #%s" % (int(last_block.index) + 1)
    prev_hash = last_block.hash
    block_hash = calculate_hash(index, prev_hash, data, timestamp)

    block_data = {}
    block_data['index'] = int(last_block.index) + 1
    block_data['timestamp'] = calculate_hash
    block_data['data'] = "I block #%s" % last_block.index
    block_data['prev_hash'] = last_block.hash
    block_data['hash'] = block_hash
    return Block(block_data)

import os
import json
from app.models.block import Block
from common import get_data_directory


def sync():
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
                block_object = Block(block_info)
                node_blocks.append(block_object)
    return node_blocks

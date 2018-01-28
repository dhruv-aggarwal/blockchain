import os
from config import blockchain_dir
import hashlib


def get_data_directory():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../')
    ) + blockchain_dir


def generate_header(index, prev_hash, data, timestamp):
    return str(index) + prev_hash + data + str(timestamp)


def calculate_hash(index, prev_hash, data, timestamp):
    header_string = generate_header(index, prev_hash, data, timestamp)
    sha = hashlib.sha256()
    sha.update(header_string)
    return sha.hexdigest()


def get_block_filename(index):
    return '%s/%s.json' % (get_data_directory(), index)

import os
from app import app
import hashlib

blockchain_dir = app.config['BLOCKCHAIN_DIR']


def get_data_directory():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../')
    ) + '/' + blockchain_dir


def generate_header(index, prev_hash, data, timestamp, nonce):
    return str(index) + prev_hash + data + str(timestamp) + str(nonce)


def calculate_hash(index, prev_hash, data, timestamp, nonce):
    header_string = generate_header(index, prev_hash, data, timestamp, nonce)
    sha = hashlib.sha256()
    sha.update(header_string)
    return sha.hexdigest()


def get_block_filename(index):
    return '%s/%s.json' % (get_data_directory(), index)

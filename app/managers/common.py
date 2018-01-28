import os
from config import blockchain_dir


def get_data_directory():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../')
    ) + blockchain_dir

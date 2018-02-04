from config import num_zeores
import json
from app.managers.common import get_block_filename


class Block(object):
    def __init__(self, **kwargs):
        """
        Initialise a block in the blockchain

        :param index: The index for the number of blocks in the chain
        :type index: int
        :param hash: The hash specific for this block
        :type hash: basestring
        :param timestamp: The time when this block was created
        :type timestamp: int
        :param data: Data contained by this block
        :type data: str (json)
        :param prev_hash: The hash for the previous block in the chain
        :type prev_hash: str
        :param nonce: For identifying unique requests
        :type nonce: str
        """
        self.block_data_types = {
            'index': int,
            'nonce': int,
            'hash': str,
            'prev_hash': str,
            'timestamp': int,
            'data': str
        }
        for key, value in kwargs.iteritems():
            if key in self.block_data_types:
                setattr(self, key, self.block_data_types[key](value))
            else:
                setattr(self, key, value)

    def __dict__(self):
        return {
            'index': str(self.index),
            'timestamp': str(self.timestamp),
            'prev_hash': str(self.prev_hash),
            'hash': str(self.hash),
            'data': str(self.data),
            'nonce': str(self.nonce)
        }

    def __eq__(self, other):
        return (
            self.index == other.index and
            self.timestamp == other.timestamp and
            self.prev_hash == other.prev_hash and
            self.hash == other.hash and
            self.data == other.data and
            self.nonce == other.nonce
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "Block<prev_hash: %s,hash: %s>" % (self.prev_hash, self.hash)

    def is_valid(self):
        """
        Current validity is only that the hash begins with at least NUM_ZEROS
        """
        if str(self.hash[0:num_zeores]) == '0' * num_zeores:
            return True
        return False

    def save(self):
        # Fill the index with leading zeroes so that we can see the files in
        # alphabetical order
        filename = get_block_filename(str(self.index).zfill(8))
        with open(filename, 'w') as block_file:
            json.dump(self.__dict__(), block_file)

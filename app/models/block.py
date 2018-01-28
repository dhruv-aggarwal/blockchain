class Block(object):
    def __init__(self, **kwargs):
        """
        Initialise a block in the blockchain

        :param index: The index for the number of blocks in the chain
        :type index: int
        :param hash: The hash specific for this block
        :type index: basestring
        :param timestamp: The time when this block was created
        :type index: int
        :param data: Data contained by this block
        :type index: str (json)
        :param prev_hash: The hash for the previous block in the chain
        :type index: str
        """
        self.index = kwargs.get('index')
        self.hash = kwargs.get('hash')
        self.timestamp = kwargs.get('timestamp')
        self.data = kwargs.get('data')
        self.prev_hash = kwargs.get('prev_hash')

    def __dict__(self):
        return {
            'index': str(self.index),
            'timestamp': str(self.timestamp),
            'prev_hash': str(self.prev_hash),
            'hash': str(self.hash),
            'data': str(self.data)
        }

    def __str__(self):
        return "Block<prev_hash: %s,hash: %s>" % (self.prev_hash, self.hash)

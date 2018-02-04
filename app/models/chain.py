class Chain:
    def __init__(self, blocks):
        self.blocks = blocks

    def is_valid(self):
        '''
        Is a valid blockchain if
        1) Each block is indexed one after the other
        2) Each block's prev hash is the hash of the prev block
        3) The block's hash is valid for the number of zeros
        '''
        for index, cur_block in enumerate(self.blocks[1:]):
            prev_block = self.blocks[index]
            if prev_block.index + 1 != cur_block.index:
                return False
            if not cur_block.is_valid():
                return False
            if prev_block.hash != cur_block.prev_hash:
                return False
        return True

    def save(self):
        '''
        Save the blockchain to the file system
        '''
        for block in self.blocks:
            block.save()

    def find_block_by_hash(self, b_hash):
        for block in self.blocks:
            if block.hash == b_hash:
                return block
        return None

    def find_block_by_index(self, index):
        if len(self) <= index:
            return self.blocks[index]
        else:
            return False

    def __len__(self):
        return len(self.blocks)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for self_block, other_block in zip(self.blocks, other.blocks):
            if self_block != other_block:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def max_index(self):
        '''
          We're assuming a valid chain. Might change later
        '''
        return self.blocks[-1].index

    def add_block(self, new_block):
        '''
          Put the new block into the index that the block is asking.
          That is, if the index is of one that currently exists, the new block
          would take it's place. Then we want to see if that block is valid.
          If it isn't, then we ditch the new block and return False.
        '''
        self.blocks.append(new_block)
        return True

    def block_list_dict(self):
        return [b.to_dict() for b in self.blocks]

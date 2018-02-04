from app.models.block import Block
from app.models.chain import Chain
from static.test import test_data

block_zero_dir = test_data[0]
block_one_dir = test_data[1]
block_two_dir = test_data[2]
block_three_dir = test_data[3]
block_three_later_in_time_dir = test_data[4]

###########################
#
# Block time
#
###########################

block_zero = Block(**block_zero_dir)
another_block_zero = Block(**block_zero_dir)
assert block_zero.is_valid()
assert block_zero == another_block_zero
assert not block_zero != another_block_zero

block_one = Block(**block_one_dir)
another_block_one = Block(**block_one_dir)
assert block_one.is_valid()
assert block_one == another_block_one
assert not block_one != another_block_one

block_two = Block(**block_two_dir)
another_block_two = Block(**block_two_dir)
assert block_two.is_valid()
assert block_two == another_block_two
assert not block_two != another_block_two

block_three = Block(**block_three_dir)
another_block_three = Block(**block_three_dir)
assert block_three.is_valid()
assert block_three == another_block_three
assert not block_three != another_block_three

#####################################
#
# Bringing Chains into play
#
#####################################
blockchain = Chain([block_zero, block_one, block_two])
assert blockchain.is_valid()
assert len(blockchain) == 3

empty_chain = Chain([])
assert len(empty_chain) == 0
empty_chain.add_block(block_zero)
assert len(empty_chain) == 1
empty_chain = Chain([])
assert len(empty_chain) == 0

another_blockchain = Chain([block_zero, block_one, block_two])
assert another_blockchain.is_valid()
assert len(another_blockchain) == 3

print another_blockchain, blockchain

assert blockchain == another_blockchain
assert not blockchain != another_blockchain
assert blockchain <= another_blockchain
assert blockchain >= another_blockchain
assert not blockchain > another_blockchain
assert not another_blockchain < blockchain

blockchain.add_block(block_three)
assert blockchain.is_valid()
assert len(blockchain) == 4
assert not blockchain == another_blockchain
assert blockchain != another_blockchain
assert not blockchain <= another_blockchain
assert blockchain >= another_blockchain
assert blockchain > another_blockchain
assert another_blockchain < blockchain

blockchain.save()

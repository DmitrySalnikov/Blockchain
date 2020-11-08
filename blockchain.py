from block import Block
from transaction import Transaction
from pyllist import sllist


class Blockchain:
    __TARGET_BITS = 4

    def __init__(self):
        """Initialize blockchain"""

        genesys_block = self.__mine(Block([Transaction("")], self.__valid_block_start()))
        self.__chain = sllist([genesys_block])

    def add_transaction(self, transaction):
        block = self.__mine(Block([transaction], self.__chain.first.value.hash()))
        self.__chain.appendleft(block)

    def print_blocks_data(self, n=0):
        """print all blocks data if n equal 0"""

        if n <= 0 or n >= self.__chain.size:
            n = self.__chain.size - 1

        current_block = self.__chain.first
        for _ in range(n):
            print(current_block.value.data())
            current_block = current_block.next
        return n

    def __mine(self, block):
        while not self.__validation(block):
            block.nonce += 1
        return block

    def __validation(self, block):
        return block.hash()[:self.__TARGET_BITS] == self.__valid_block_start()

    def __valid_block_start(self):
        return '0' * self.__TARGET_BITS

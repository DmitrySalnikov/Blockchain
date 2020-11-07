from block import Block
from pyllist import sllist


class Blockchain:
    __TARGET_BITS = 4

    def __init__(self):
        """Initialize blockchain"""

        self.__chain = sllist([Block("", 0, '0' * self.__TARGET_BITS)]) # add PoW for first block?

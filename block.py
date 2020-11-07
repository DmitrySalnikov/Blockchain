from datetime import datetime
from hashlib import sha256


class Block:

    def __init__(self, message, nonce, previous_hash):
        """Initialize block"""

        self.__message = message
        self.__nonce = nonce
        self.__previous_hash = previous_hash
        self.__timestamp = datetime.utcnow()

    def __block_str(self):
        return '{}{}{}{}'.format(self.__message, self.__nonce, self.__previous_hash, self.__timestamp)

    def hash(self):
        return sha256(self.__block_str().encode()).hexdigest()

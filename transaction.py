class Transaction:

    def __init__(self, message):
        self.__message = message

    def data(self):
        return self.__message

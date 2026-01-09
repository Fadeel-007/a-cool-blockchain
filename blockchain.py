class blockchain(object):
    def __init__(self):
        # lets initiate empty lists to store block and transactions
        self.chain = []
        self.current_transactions = []

    # method to create a new block
    def new_block(self):
        pass

    # method to create a new transaction
    def new_transaction(self):
        pass

    # we'll hash a block with this one
    @staticmethod
    def hash(block):
        pass

    # method to get the last block
    @property
    def last_block(self):
        pass

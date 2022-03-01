class Category:
    amount = 0
    description = ""
    ledger = list()
    ledger = []
    def __init__(self, description) -> None:
        print("init")
    def deposit(self,amount,description):
        self.amount = amount
        self.description = description

    def withdraw(self,amount,description):
        print("withdraw")
    
    def get_balance(self):
        print("balance")

    def check_funds(self,amount) -> bool:
        if amount > self.amount:
            return False
        else:
            return True
    def transfer(self,amount,category) -> bool:
        print("transfer")
        return False


def create_spend_chart(categories:Category):
    print("create!")
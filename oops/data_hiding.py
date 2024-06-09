class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    # Implement data hiding
    def get_balance(self):
        return self.__balance


t = Account(1100)

# print(t.balance)
print(t.get_balance())
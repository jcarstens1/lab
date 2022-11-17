class Account:
    def __init__(self, name):
        '''
        Function to create an account with a person's name and account balance
        :param name: Account name
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        '''
        Function to increment the account balance by the specified amount
        :param amount: Amount to deposit
        :return: False if deposit is unsuccessful, True if deposit is successful
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount):
        '''
        Function to decrement the account balance by the specified amount
        :param amount: Amount to withdrawal
        :return: False if withdrawal is unsuccessful, True if withdrawal is successful
        '''
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self):
        '''
        Function to return the account balance
        :return: Account balance
        '''
        return self.__account_balance

    def get_name(self):
        '''
        Function to return the account name
        :return: Account name
        '''
        return self.__account_name

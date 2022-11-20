from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('James')
        self.p2 = Account('Sydney')
        self.p2.deposit(100)

    def test_init(self):
        assert self.p1.get_name() == 'James'
        assert self.p1.get_balance() == 0
        assert self.p2.get_name() == 'Sydney'
        assert self.p2.get_balance() == 100

    def test_deposit(self):
        assert self.p1.deposit(100) is True
        assert self.p1.get_balance() == 100
        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == 100
        assert self.p1.deposit(-1) is False
        assert self.p1.get_balance() == 100
        assert self.p2.deposit(100) is True
        assert self.p2.get_balance() == 200
        assert self.p2.deposit(0) is False
        assert self.p2.get_balance() == 200
        assert self.p2.deposit(-1) is False
        assert self.p2.get_balance() == 200

    def test_withdraw(self):
        self.p1.deposit(1)
        assert self.p1.withdraw(1) is True
        assert self.p1.get_balance() == 0
        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == 0
        assert self.p1.withdraw(-1) is False
        assert self.p1.get_balance() == 0
        assert self.p2.withdraw(100) is True
        assert self.p2.get_balance() == 0
        assert self.p2.withdraw(0) is False
        assert self.p2.get_balance() == 0
        assert self.p2.withdraw(-1) is False
        assert self.p2.get_balance() == 0

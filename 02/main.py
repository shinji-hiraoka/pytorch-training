from bank_account import BankAccount

if __name__ == "__main__":

    account = BankAccount("Taro")

    print("初期残高:", account.get_balance())

    account.deposit(10000)
    print("入金後:", account.get_balance())

    account.withdraw(3000)
    print("出金後:", account.get_balance())

    account.set_interest_rate(0.05)
    account.apply_interest()

    print("利息適用後:", account.get_balance())
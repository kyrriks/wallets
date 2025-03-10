from wallets.models import Wallet


def deposit(wallet: Wallet, amount: float):
    wallet.balance += amount
    wallet.save()


def withdraw(wallet: Wallet, amount: float):
    if wallet.balance - amount < 0:
        raise ValueError('Недостаточно средств на счете')
    wallet.balance -= amount
    wallet.save()
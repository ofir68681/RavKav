from __future__ import annotations
import random
from profile import Profile


# The class represent the RavKa card, and provides all its functionalities.
class RavKavCard:

    def __init__(self, id_num: int, user_profile: str, money: float):
        self.id_num = id_num
        self.profile: Profile = Profile[user_profile]
        self.money = money

    def __str__(self):
        return f'id: {self.id_num}, profile: {self.profile.name}, money must be funny: {self.money}'

    # Deposition of money to the card.
    def deposit(self, payment: float) -> None:
        if self.profile == Profile.Old:
            self.money += payment * 1.5
        elif self.profile in {Profile.Young, Profile.Student}:
            self.money += payment * 1.33
        else:
            print("eat shit")

    # pay for a ride.
    def pay(self, m: float) -> None:
        if self.money >= m:
            self.money -= m
        else:
            print("die")

    # check how much money do you have on your card.
    def check_money(self) -> float:
        return self.money

    # Generates a random card.
    @staticmethod
    def auto_user():
        while True:
            p = random.choice(list(Profile))
            money = random.randint(0, 200)
            id_num = random.randint(111111111, 999999999)
            yield RavKavCard(id_num=id_num, user_profile=p.name, money=money)


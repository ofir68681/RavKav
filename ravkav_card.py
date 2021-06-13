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
        if self.profile == Profile.old:
            self.money += payment * 1.5
        elif self.profile in {Profile.young, Profile.student}:
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

# Returns a random card.
    @staticmethod
    def rand_card() -> RavKavCard:
        id_num = random.randint(1, 999999999)
        profiles = ["young", "student", "old"]
        profile = random.choice(profiles)
        money = random.randint(0, 1000)
        return RavKavCard(id_num, profile, money)



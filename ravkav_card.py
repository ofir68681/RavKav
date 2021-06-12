import random
from profile import Profile


class RavKavCard:

    def __init__(self, id_num: int, user_profile: str, money: float):
        self.id_num = id_num
        self.profile: Profile = Profile[user_profile]
        self.money = money

    def __str__(self):
        return f'id: {self.id_num}, profile: {self.profile.name}, money must be funny: {self.money}'

    def deposit(self, payment: float):
        if self.profile == Profile.old:
            self.money += payment * 1.5
        elif self.profile in {Profile.young, Profile.student}:
            self.money += payment * 1.33
        else:
            print("eat shit")

    def pay(self, m):
        if self.money >= m:
            self.money -= m
        else:
            print("die")

    def check_money(self):
        return self.money

    @staticmethod
    def rand_card():
        id_num = random.randint(1, 999999999)
        profiles = ["young", "student", "old"]
        profile = random.choice(profiles)
        money = random.randint(0, 1000)
        return RavKavCard(id_num, profile, money)

    def menu(self):
        while True:
            print("Select action: \n 1.Check balance. \n 2.Pay for a ride. \n 3.Deposit.")
            choice = int(input("Enter your selection: "))
            if choice == 1:
                print(self.check_money())
            elif choice == 2:
                amount = int(input("How much you want to pay?"))
                self.pay(amount)
                print("You got now:", self.check_money())
            elif choice == 3:
                amount = int(input("How much you want to deposit?"))
                self.deposit(amount)
                print("You got now:", self.check_money())

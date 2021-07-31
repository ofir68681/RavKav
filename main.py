import ravkav_card
from ravkav_card import RavKavCard

if __name__ == '__main__':
    # crd1 = RavKavCard(314962101, "Young", 90)
    # print(crd1)
    # crd1.deposit(100)
    # print(crd1)
    # crd1.pay(10)
    # print(crd1)
    # crd1.pay(100000)
    # crd1.menu()
    profile_generator = RavKavCard.auto_user()

    for i in range(3):
        new_user = next(profile_generator)
        print(new_user)

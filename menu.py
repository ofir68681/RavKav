from ravkav_card import RavKavCard

# Menu for RavKav users.
def menu(crd: RavKavCard) -> None:
    while True:
        print("Select action: \n 1.Check balance. \n 2.Pay for a ride. \n 3.Deposit.")
        choice = int(input("Enter your selection: "))
        if choice == 1:
            print(crd.check_money())
        elif choice == 2:
            amount = int(input("How much you want to pay?"))
            crd.pay(amount)
            print("You got now:", crd.check_money())
        elif choice == 3:
            amount = int(input("How much you want to deposit?"))
            crd.deposit(amount)
            print("You got now:", crd.check_money())

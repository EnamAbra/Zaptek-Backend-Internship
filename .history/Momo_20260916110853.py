intro = """ Unlock more deals and try our new MoMo app!"""
print(intro)
print("1) Transfer Money")
print("2) MoMoPay & Pay Bills")
print("3)  Airtime & Bundles")
print("4)  Allow Cashout")
print("5)  Financial")
print("6)  My Wallet")
print("7)  Just4U")
print("8)  MoMo App")
balance = 100
result1 = input("Please select an option (1-8): ")
if result1 == "6":
    print("1) Check Balance")
    print("2) Allow Cash out")
    print("3) My Approvals")
    print("4) Report Fraud")
    print("5) Statements")
    result2 = input("Please select an option (1-5): ")
    if result2 == "1":
        pin = input("Please enter your momo pin:")
        if pin == "2345":
            print(f"Your balance is ₵{balance:.2f}")
        else:
            print("Incorrect pin. Please try again.")
    elif result2 == "2" or result2 == "3" or result2 == "4" or result2 == "5" :
        print("Invalid Option.Please Try again")


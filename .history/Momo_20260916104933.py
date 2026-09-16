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
        print("Please enter your momo pin:")
        if int(input()) == 2345:
            print("Your balance is {balance}:")

        else:
            print("Incorrect pin. Please try again.")
    elif result2 == "2":
      
        print("Invalid Option. Please try again.")
    elif result2 == "3":
        print("Invalid Option. Please try again.")
    elif result2 == "4":
        print("Invalid Option. Please try again.")
    else:
        print("Invalid option selected.")
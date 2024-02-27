usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == 'egalong' and passwordInput == '356897':
    print('Loged In')
    print("---Welcome to Stargazer Shop---")
    print("1.Chocolate Bar   120 THB/Piece")
    print("2.Brownie          75 THB/Piece")
    print("3.Potato Chips     35 THB/Piece")
    UserSelected = int(input("Select Products Number>>"))
    if UserSelected == 1:
        amount = int(input("Please Enter amount : "))
        print("Total Price:", str(120*amount), "THB")
    elif UserSelected == 2:
        amount = int(input("Please Enter amount : "))
        print("Total Price:", str(75*amount), "THB")
    elif UserSelected == 3:
        amount = int(input("Please Enter amount : "))
        print("Total Price:", str(35*amount), "THB")
else:
    print("---ERROR---")

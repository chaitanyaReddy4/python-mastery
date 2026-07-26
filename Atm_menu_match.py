#This is done using match case------
print("ATM Menu")
print("1 → Deposit")
print("2 → Withdraw")
print("3 → Check Balance")
print("4 → Exit")

choice=int(input("Enter your selection:"))
match choice:
    case 1:
        print("Deposit")
    case 2:
        print("Withdraw")
    case 3:
        print(" Check balance")
    case 4:
        print("Exit")
    case _:
        print("Invalid input")
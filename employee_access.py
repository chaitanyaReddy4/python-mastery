employee=int(input("Enter your employee ID: "))
password=input("Enter your password: ")
deptartment=input("Enter your department: ")
if employee==1435:
    if password=="admin143":
        if deptartment=="IT":
            print("Access granted")
        else:
            print("Access denied: Incorrect department")
    else:
        print("Access denied: Incorrect password")
else:
    print("Access denied: Incorrect employee ID")


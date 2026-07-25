employee=int(input("Enter your employee ID: "))
password=input("Enter your password: ")
department=input("Enter your department: ")
is_admin = input("Are you admin (yes/no): ").lower() == "yes"
if employee==1432 and password=="admin1431":
    if department=="IT" or is_admin:
        print("access granted")
    else:
        print("INCORRECT DEPT OR NOT ADMIN.")
else:
    print("INCORRECT EMPLOYEE ID OR PASSWORD")

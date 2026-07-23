name=input("Enter your name: ")
branch=input("Enter your branch: ")
roll_no=int(input("Enter your roll number: "))
maths=int(input("Enter your Maths marks: "))
physics=int(input("Enter your Physics marks: "))
chemistry=int(input("Enter your Chemistry marks: "))
total_marks=maths+physics+chemistry
average_marks=total_marks/3

print("******Student Report******")
print(f"Name: {name}")
print(f"Branch: {branch}")
print(f"Roll Number: {roll_no}")
print(f"\nMaths Marks: {maths}")
print(f"Physics Marks: {physics}")
print(f"Chemistry Marks: {chemistry}")
print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")

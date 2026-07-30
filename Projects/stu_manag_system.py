stu_marks=[]
while True:
  print()
  print(f"*******Student Manager********** \n 1. Add Student Marks \n 2. Display Marks\n 3. Statistics\n 4. Search Student \n 5. Star Pattern \n 6. Exit ")
  choice=int(input("enter your choice:"))
  if choice==1:
    no_studen=int(input("enter no of students:"))
    for i in range(1,no_studen+1):
      marks=float(input(f"enter marks of student {i}:"))
      if marks<0:
        print("invalid marks!")
        continue
      stu_marks.append(marks)
    print("------marks added succesfully!-----")
  elif choice==2:
    if len(stu_marks)==0:
      print("No data found!")
      continue
    for j in range(len(stu_marks)):
      print(f"student {j+1} is :{stu_marks[j]}")
  elif choice==3:
    if len(stu_marks)==0:
      print("no marks are added yet.add marks by choosing 1 choice.")
      continue
    total=0
    avg=0
    high=stu_marks[0]
    low=stu_marks[0]
    even=0
    odd=0
    for k in stu_marks:
      total=total+k
      if k>high:
        high=k
      if k<low:
        low=k
      if k%2==0:
        even=even+1
      else:
        odd=odd+1
    print("highest is:\t",high)
    print("lowest is:\t",low)
    print("even are:\t",even)
    print("odd are:\t",odd)
    print("total is :\t",total)
    avg=total/len(stu_marks)
    print("avg is:\t",avg)
  elif choice==4:
    a=int(input("enter mark to search:\t "))
    for mark in stu_marks:
      if mark==a:
         print("Found!")
         break
    else:
        print("NOT FOUND!")
  elif choice==5:
    rows=int(input("enter rows: "))
    for i in range(rows+1):
      for j in range(i):
        print("*",end=" ")
      print()
    print()
    for i in range(rows,0,-1):
      for j in range(i):
        print("*",end=" ")
      print()
  elif choice==6:
    print("exit")
    break
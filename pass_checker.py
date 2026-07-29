#using while loops

password="rajesh"
while True:
  a=input("enter password: ")
  if a==password:
    print("success")
    break
  print("wrong password:",a)
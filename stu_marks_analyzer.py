#iterating over collections..

marks = [85,92,76,88,95]
total=0
high=marks[0]
low=marks[0]
for i in marks:
  total=total+i
  if i>high:
    high=i
  if i<low:
    low=i
print(total)
avg=total/len(marks)
print(avg)
print(high)
print(low)
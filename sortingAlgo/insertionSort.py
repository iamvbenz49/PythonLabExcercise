l = []
n = int(input("enter the number of elemnts : "))
for i in range(n):
  c = int(input("enter the number : "))
  l.append(c)
print("the list is ",l)
for i in range(1,len(l)):
  j = i-1
  key = l[i]
  while l[j]>key and j>=0:
    l[j+1] = l[j]
    j-=1
  l[j+1]=key
print("the sorted list is ",l)

a = []
rows = int(input("ENTER THE NUMBER OF ROWS : "))
cols = int(input("ENTER THE NUMBER OF COLUMNS : "))
for i in range(rows):
  a.append([])
  for j in range(cols):
    num = int(input("enter the element : "))
    a[i].append(num)
b = []
for i in range(rows):
  b.append([])
  for j in range(cols):
    num = int(input("enter the element : "))
    b[i].append(num)
c = []
for i in range(rows):
  c.append([])
  for j in range(cols):
    c[i].append(a[i][j]+b[i][j])
for i in range(rows):
  for j in range(cols):
    print(c[i][j],end=" ")
  print()
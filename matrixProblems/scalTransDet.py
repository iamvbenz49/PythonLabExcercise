x = [[1,3,5],
    [2,4,8],
    [13,15,17]]
scalar = trans = [[0,0,0],[0,0,0],[0,0,0]]
n = int(input("enter the scalar value : "))
for i in range(len(x)):
  for j in range(len(x[0])):
    scalar[i][j] = n*x[i][j]
print("SCALAR MATRIX")
for i in scalar:
  print(i)
for i in range(len(x)):
  for j in range(len(x[0])):
    trans[i][j]= x[j][i]
print("TRANSPOSE MATRIX")
for i in trans:
  print(i)
a = x[0][0]
b = x[0][1]
c = x[0][2]
d = x[1][0]
e = x[1][1]
f = x[1][2]
g = x[2][0]
h = x[2][1]
i = x[2][2]
det = a*((e*i)-(f*h)) - b*((d*i)-(g*f))+c*((h*d)-(e*g))
print("DETREMINANT : ",det)
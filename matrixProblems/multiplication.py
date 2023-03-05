row1 = int(input("ENTER THE NUMBER OF ROWS MATRIX 1 : "))
col1 = int(input("ENTER THE NUMBER OF COLS MATRIX 1 : "))
row2 = int(input("ENTER THE NUMBER OF ROWS MATRIX 2 : "))
col2 = int(input("ENTER THE NUMBER OF COLS MATRIX 1 : "))

if row1 == col2:
  print("enter the element in first matrix")
  x = [[int(input()) for i in range(col1)] for j in range(row1)]
  print("enter the element in second matrix")
  y = [[int(input()) for i in range(col2)] for j in range(row2)]
  result = [[0 for i in range(col2)] for j in range(row1)]
  print("The matrix X : ",x)
  print("The matrix Y : ",Y)
  for i in range(row1):
    for j in range(col2):
      for k in range(len(y)):
        result[i][j] += x[i][k]*y[k][j]
  print("The multiplication matrix is ")
  for i in range(row1):
    print(result)
else:
  print("multiplication not possible")

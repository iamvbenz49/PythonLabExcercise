def towerOfHanoi(n,source,dest,aux):
  if n==1:
    print("move disk 1 form ",source," to ",dest)
    return n
  else:
    towerOfHanoi(n-1,source,aux,dest)
    print("move disk",n,"form",source," to ",dest)
    towerOfHanoi(n-1,aux,dest,source)
n = int(input("enter the number : "))
towerOfHanoi(n,'A',"b",'C')
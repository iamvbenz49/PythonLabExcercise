l = [1,2,3,4]
s = 0
e = 3
while s<=e:
  m = s + (e-s)//2
  if l[m]==4:       
    print(m+1)
    break
  elif l[m]>4:
    e=m-1
  else:
    s=m+1

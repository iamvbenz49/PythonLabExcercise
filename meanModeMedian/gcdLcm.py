def gcd(a,b):
  res = 1
  for i in range(1,a+1):
    if a%i==0 and b%i==0:
      res = i
  return res
print(gcd(20,35))
print("LCM ",(20*35)//gcd(20,35))
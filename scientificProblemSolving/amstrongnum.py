num = int(input("ENTER THE NUMBER : "))
temp = num 
s = 0
while num>0:
  rem = num%10
  s+=rem**3
  num//=10
if temp == sum:
  print("AMSTRONG")
else:
  print("NOT AMSTRONG")
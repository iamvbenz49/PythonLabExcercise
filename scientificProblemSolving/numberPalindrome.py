n = int(input("ENTER THE NUMBER : "))
temp = n
s =0
while n>0:
  rem = n%10
  s = (s*10)+rem
  n//=10
if temp == s:
  print("PALINDROME")
else:
  print("NOT PALINDROME")
def anagram(s1,s2):
  n1 = len(s1)
  n2 = len(s2)
  if n1!=n2:
    return 0
  s1 = sorted(s1)
  s2 = sorted(s2)
  for i in range(n1):
    if s1[i]!=s2[i]:
      return 0
  return 1
str1 = input("enter string1 : ")
str2 = input("enter string2 : ")
str1 = str1.lower()
str2 = str2.lower()
if anagram(str1,str2):
  print("ANAGRAM")
else:
  print("NOT ANAGRAM")
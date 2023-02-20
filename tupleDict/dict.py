s = "programming"
dic = {}
for i in s:
  dic.setdefault(i,0)
  dic[i]+=1
for i in dic:
  print(i,":",dic[i])
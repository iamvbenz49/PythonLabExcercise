def mean(n,list):
  s =sum(list)
  mean = s/n
  return mean
def median(list,n):
  if n%2==0:
    m1 = list[(n//2)-1]
    m2 = list[(n//2)]
    m = (m1+m2)/2
  else:
    m = list[n//2]
  return m
def mode(list):
  fre = { }
  for i in list:
    fre.setdefault(i,0)
    fre[i]+=1
  m = max(fre.values())
  high = []
  for i in fre:
    if fre[i]==m:
      high.append(i)
  return high
l = [2,1,3,2,1]
print(mean(5,l))
print(median(l,5))
print(mode(l))
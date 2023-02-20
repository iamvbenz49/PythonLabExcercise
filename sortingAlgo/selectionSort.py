l = [1,2,3,4,5,6,7,8,9]
for i in range(len(l)-1):
  min_idx = i
  for j in range(i+1,len(l)-1):
    if(l[min_idx]>l[j]):
      min_idx = j
  l[min_idx],l[i] = l[i],l[min_idx]
print(l)
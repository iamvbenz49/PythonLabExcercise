def dups(arr):
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if(arr[i]==arr[j]):
        print(arr[i])
arr = [1,2,3,4,2,7,8,8,3]
dups(arr)
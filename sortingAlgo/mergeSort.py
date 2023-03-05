def merge(l,r,A):
  i ,j , k = 0,0,0
  while i<len(l) and j<len(r):
    if l[i]>r[j]:
      A[k]=r[j]
      j+=1
    else:
      A[k]=l[i]
      i+=1
    k+=1
  while i<len(l):
    A[k]=l[i]
    i+=1
    k+=1
  while j<len(r):
    A[k]=r[j]
    j+=1
    k+=1
def mergeSort(A):
  n = len(A)
  if n>1:
    m = n//2
    l = A[:m]
    r = A[m:]
    mergeSort(l)
    mergeSort(r)
    merge(l,r,A)
  #  print(A)
A = [1,2,3,4,5,6,7,8,9]
mergeSort(A)
print(A)

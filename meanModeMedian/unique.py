def unique(lst):
  l = []
  for i in lst:
    if i not in l:
      l.append(i)
  print(*l)
unique([10,20,10,30,40,40])
def make_change(n,m):
  if n == 0:
    return 1
  if n < 0 :
    return 0
  if m <= 0 and n >= 1:
    return 0



print(make_change(20,5))
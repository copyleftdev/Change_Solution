


def change(n,coins_available, coins_so_far):
  if sum(coins_so_far) == n:
    yield coins_so_far
  elif sum(coins_so_far) > n:
    pass
  elif coins_available == []:
    pass

  else:
    for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
      yield c
    for c in change(n, coins_available[1:], coins_so_far):
      yield c

def change_optimized (n,coins):
  solution = [s for s in change(n,coins,[])]
  return  min(solution, key=len)
#TEST
n = 60
coins = [1, 5,10, 25]

# solution = [s for s in change(n, coins, [])]
# for s in solution:
#   print(s)

print 'optimal solution' , change_optimized(n, coins)
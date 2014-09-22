#!/usr/bin/env python


import os, sys

def make_change(coins, value):

  table = [None for x in range(value + 1)]
  table[0] = []

  for i in range(1, value + 1):
    for coin in coins:
      if coin > i: continue
      elif not table[i] or len(table[i - coin]) + 1 < len(table[i]):
        if table[i - coin ] != None:
          table[i] = table[i - coin][:]
          table[i].append(coin)

  if table[-1] != None:
    print '{} coins: {}'.format(len(table[-1],table[-1]))
  else:
    print 'No solution possible'

if __name__ == '__main__':
  def usage():
    print("Usage: {} value\n".format(os.path.basename(sys.argv[0])))
    sys.exit(1)

    #Tests
    coins =  [ 200, 100, 50, 55, 43, 35, 25]

    if len(sys.argv) != 2:
      usage()
    try:
      value = int(sys.argv[1])
    except ValueError:
      usage()

    make_change(coins, value)
def rabbit_pairs(n, k):
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    return rabbit_pairs(n-1, k) + k*rabbit_pairs(n-2, k)

n = int(input('Enter the value of n (months): '))
k = int(input('Enter the value of k (no of rabbit pairs):'))

ans = rabbit_pairs(n, k)
print('Total number of rabbit pairs: ', ans)

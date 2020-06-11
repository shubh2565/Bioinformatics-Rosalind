s = 'GATATATGAGTATATGCCAGGCCATATAGCGGTCACTTATATATA'
t = 'ATAT'

print('Locations of motif ' + t + ' in the given sequence :')

for i in range(len(s) - len(t) + 1):
  if s[i:i+len(t)] == t:
    print(i + 1)

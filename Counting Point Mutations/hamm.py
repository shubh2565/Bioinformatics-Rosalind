#s = 'GAGCCTACTAACGGGAT'
#t = 'CATCGTAATGACGGCCT'

seq = []

with open('rosalind_hamm.txt') as f:
  for line in f:
    seq.append(line[:-1])

print(seq)

count = 0

for i in range(len(seq[0])):
  if seq[0][i] != seq[1][i]:
    count += 1

print('The hamming distance between the two sequence: ',count)

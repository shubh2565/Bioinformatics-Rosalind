dna_dict = {}

with open('rosalind_gc.txt') as f:
  for line in f:
    if '>Rosalind' in line:
      key = line.strip()[1:]
      dna_dict[key] = ""
    else:
      dna_dict[key] += line.strip()

print(dna_dict)

dna_gc = {}

for key, value in dna_dict.items():
  gc = 0
  for base in range(len(value)):
    if value[base] is 'G' or value[base] is 'C':
      gc += 1
  score = gc/len(value)
  dna_gc[key] = score

print(dna_gc)

import operator

top = max(dna_gc.items(), key=operator.itemgetter(1))[0]

print('ID:', top)
print('GC content: %.4f' %(dna_gc[top]*100))

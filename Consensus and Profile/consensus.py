dna_dict = {}

with open('rosalind.txt') as f:
  for line in f:
    if '>Rosalind' in line:
      key = line.strip()[1:]
      dna_dict[key] = ""
    else:
      dna_dict[key] += line.strip()

dna_list = []

for key, values in dna_dict.items():
  dna_list.append(values)

print(dna_list)

import numpy as np

profile = np.zeros((4, len(dna_list[0])))

for seq in dna_list:
  for i in range(len(seq)):
    if seq[i] == 'A':
      profile[0][i] += 1
    elif seq[i] == 'C':
      profile[1][i] += 1
    elif seq[i] == 'G':
      profile[2][i] += 1
    else:
      profile[3][i] += 1

print('Profile Matrix:\n',profile)

consensus_arg = np.argmax(profile, axis = 0)

consensus = ''

for i in consensus_arg:
  if i == 0:
    consensus += 'A'
  elif i == 1:
    consensus += 'C'
  elif i == 2:
    consensus += 'G'
  else:
    consensus += 'T'

print('Consensus String:',consensus)

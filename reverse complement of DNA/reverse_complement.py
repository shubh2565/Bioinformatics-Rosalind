#dna = 'AAAACCCGGTAGCGGTTTAAGCAGTGGGGTAACCCCT'

file = open('rosalind_dna.txt')
dna = file.read()

print("DNA strand:\n",dna)

dna_reverse = dna[::-1]

dna_rc = ""

for i in range(len(dna_reverse)):
  if dna_reverse[i] is 'A':
    dna_rc += 'T'
  elif dna_reverse[i] is 'T':
    dna_rc += 'A'
  elif dna_reverse[i] is 'G':
    dna_rc += 'C'
  elif dna_reverse[i] is 'C':
    dna_rc += 'G'

print("Reverse Complement of given DNA:\n",dna_rc)

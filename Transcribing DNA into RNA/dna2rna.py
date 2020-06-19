dna = open("rosalind_dna.txt")
dna = dna.read()

print('DNA:', dna)

print('RNA:',dna.replace('T', 'U'))

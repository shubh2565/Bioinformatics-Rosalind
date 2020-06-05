dna = open("rosalind_dna.txt")
dna = dna.read()
print(dna)

count = [0, 0, 0, 0]

for i in range(len(dna)):
    if dna[i] is 'A':
        count[0] += 1
    elif dna[i] is 'C':
        count[1] += 1
    elif dna[i] is 'G':
        count[2] += 1
    else:
        count[3] += 1

for n in count:
    print(n, end=" ")

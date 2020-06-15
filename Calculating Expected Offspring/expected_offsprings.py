"""
Genotypes:


    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa
"""

print('Enter the list of numbers representing the six genotypes: ')

x = []

for i in range(6):
  a = int(input())
  x.append(a)

print(x)

print(x)

offspring = 0

prob_dominant = [1.0, 1.0, 1.0, 0.75, 0.5, 0]

for i in range(len(x)):
  offspring += 2*prob_dominant[i]*x[i]

print('The expected number of offspring displaying the dominant phenotype:',offspring)

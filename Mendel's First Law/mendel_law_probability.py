k = int(input('Enter the number of individuals which are homozygous dominant for a factor (k):'))
m = int(input('Enter the number of individuals which are heterozygous (m):'))
n = int(input('Enter the number of individuals which are homozygous recessive for a factor (n):'))

total = k + m + n

# Total probability -
#(prob of having both homozygous recessive individual*prob of not passing a dominant allele
# + prob of having one homozygous recessive individual and one hetrozygous
# individual*prob of not passing a dominant allele
# + prob of having both heterozygous individual*prob of not passing a dominant allele)

prob = 1 - ((n/total)*((n-1)/(total-1)) + 
            2*(n/total)*(m/(total-1))*0.5 + 
            (m/total)*((m-1)/(total-1))*0.25)

print('The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele:', prob)

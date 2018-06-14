#Project Euler 1
#sum of all multiples of 3 and 5 below 1000, (not including 1000)

total=0
numlist = []
for i in range(1000):
    if i % 3 == 0:
        numlist.append(i)
    elif i % 5 == 0:
        numlist.append(i)

print(sum(numlist))


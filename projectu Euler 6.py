#project Euler problem 5
#Sumsquare difference
#find the diference between the sum od the squares of the first 100 numbers
#and th square of the summ of the first 100 numbers.

#(1^2+ 2^2+...) - (1+2+3+...)^2 = ?
#solved by crteaing two separate list


numlist = []
square_list = []

for i in range(101):
    numlist.append(i)
    i = i**2
    square_list.append(i)

#print(numlist)
#print(square_list)
    
num_sum = (sum(numlist))**2
square_sum = sum(square_list)

difference = num_sum - square_sum
print(difference)

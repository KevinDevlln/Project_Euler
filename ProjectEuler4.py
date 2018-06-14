#Euler problem 4
#largest palindrome

p_list = []
x=0

for i in range(99, 1000, 1):
    for j in range(1000, 99, -1):
        p = i*j
        p = str(p)
        if p == str(p)[::-1]:
            x = x+1
            p = int(p)
            p_list.append(p)

print(max(p_list))

list1 = []

num = [1,2,3,4,5,6,7,8,9,10]
for n in num :
    list1.append(n)
print(list1)

# above code = 

list1 = [n for n in num]


list2 = []

for n in num :
    if n%2==0 :
        list2.append(n)

# = 

list2 = [n for n in num if n%2 == 0]



the_list = [1,2,3,4,5]
new_list = list()

for i in the_list:
    a = 1
    for j in the_list:
        if not i == j:
            a *= j 
    new_list.append(a)

print(the_list)
print(new_list)
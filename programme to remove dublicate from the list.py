list_1=[1,2,3,1,4,56,6]
print(list(set(list_1)))
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))
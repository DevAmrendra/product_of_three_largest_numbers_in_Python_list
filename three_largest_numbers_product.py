# Imagine you have a list of integers. Write a Python program to find the three elements such that the product is maximum. If there are multiple solutions, return the one with the highest product.



input_list = [1, -2, -3, 4, 0, 6, -7, -8, 9]
big_num =min(input_list)
teen = []
pro = 1
for _ in range(3):
    for i in input_list:
        if (i > big_num):
            big_num = i
    teen.append(big_num)
    input_list.remove(big_num)
    big_num = min(input_list)

for j in teen:
    pro = pro * j
print(pro)
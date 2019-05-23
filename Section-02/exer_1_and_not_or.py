# example :
num_1 = 10
num_2 = 20
num_3 = 30
num_4 = 40
num_5 = 12
result_1 = (num_1 < num_5 < num_2) or (num_3 < num_5 < num_4)
print(result_1)
result_2 = (num_1 < num_5 < num_4) and not (num_2 < num_5 < num_3)
print(result_2)

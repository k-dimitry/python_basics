my_lst = [0] * 101

inp_lst = [int(i) for i in input().split()]

for i in inp_lst:
    my_lst[i] += 1

for i in range(len(my_lst)):
    print((str(i) + " ") * my_lst[i], end="")

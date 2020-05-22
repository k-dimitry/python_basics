def sum_of_seq():
    num = int(input())
    if num == 0:
        return 0
    else:
        num += sum_of_seq()
        return num


print(sum_of_seq())

def reverse_seq():
    num = int(input())
    if num == 0:
        print(num)
        return
    reverse_seq()
    print(num)


reverse_seq()

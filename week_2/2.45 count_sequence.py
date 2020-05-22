saved_num = current_num = int(input())
max_count = 0
counter = 0

while current_num != 0:
    if saved_num == current_num:
        counter += 1
    else:
        saved_num = current_num
        if counter > max_count:
            max_count = counter
        counter = 1
    current_num = int(input())

if counter > max_count:
    max_count = counter

print(max_count)

nums = [int(i) for i in input().split()]
max_num = nums[0]
max_count = nums.count(max_num)
for n in nums:
    if n == max_num:
        continue
    else:
        new_count = nums.count(n)
        if new_count > max_count:
            max_count = new_count
            max_num = n

print(max_num)

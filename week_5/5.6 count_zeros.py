# n = int(input())
# counter = 0
#
# for _ in range(n):
#     if int(input()) == 0:
#         counter += 1
#
# print(counter)
print(sum(int(input()) == 0 for _ in range(int(input()))))

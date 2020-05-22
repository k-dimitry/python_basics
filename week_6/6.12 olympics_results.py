n = int(input())
results = [input().split() for i in range(n)]

for result in sorted(results, key=lambda x: int(x[1]), reverse=True):
    print(result[0])

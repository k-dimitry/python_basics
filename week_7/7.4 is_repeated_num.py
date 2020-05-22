myset = set()

for i in input().split():
    if int(i) in myset:
        print("YES")
    else:
        print("NO")
        myset.add(int(i))

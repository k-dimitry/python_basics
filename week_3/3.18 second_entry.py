string = input()
first = string.find("f")
if first == -1:
    print(-2)
else:
    print(string.find("f", first + 1))

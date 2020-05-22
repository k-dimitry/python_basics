string = input()
first, last = string.find("h"), string.rfind("h")
print(string[:first + 1] + string[first + 1:last] * 2 + string[last:])

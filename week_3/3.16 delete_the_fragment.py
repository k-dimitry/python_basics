string = input()
first, last = string.find("h"), string.rfind("h")
print(string[:first] + string[last + 1:])

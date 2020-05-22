string = input()
first = string.find("h")
last = string.rfind("h")
print(string[:first + 1] +
      string[first + 1: last].replace("h", "H") + string[last:])

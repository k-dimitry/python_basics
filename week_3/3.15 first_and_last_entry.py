string = input()
first_entry = string.find("f")
if first_entry != -1:
    print(first_entry, end=" ")
    last_entry = string[::-1].find("f")
    last_entry = len(string) - last_entry - 1
    if last_entry != first_entry:
        print(last_entry)

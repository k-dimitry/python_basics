n = int(input())
guessed_nums = set(map(str, range(1, n + 1)))

while True:
    enter = input().strip()
    if enter == "HELP":
        break
    set_of_nums = set(enter.split())
    command = input().strip()
    if command == "YES":
        guessed_nums &= set_of_nums
    elif command == "NO":
        guessed_nums -= set_of_nums

print(*sorted(guessed_nums))

lst_of_sets = []
total_set = set()
n = int(input())
for _ in range(n):
    m = int(input())
    new_set = set()
    for _ in range(m):
        lang = input().strip()
        new_set.add(lang)
        total_set.add(lang)
    lst_of_sets.append(new_set)

unique_set = total_set.copy()

for student in lst_of_sets:
    unique_set &= student
print(len(unique_set), *unique_set, sep="\n")
print(len(total_set), *total_set, sep="\n")

lst_of_scores = []

with open("input.txt", "r", encoding="utf8") as f:
    k = int(f.readline())
    for line in f:
        line = line.strip().split()
        if not line:
            continue
        a, b, c = map(int, (line[-3], line[-2], line[-1]))
        if a < 40 or b < 40 or c < 40:
            continue
        # print(a, b, c)
        lst_of_scores.append(a + b + c)

lst_of_scores = sorted(lst_of_scores, reverse=True)

found = False
if len(lst_of_scores) <= k or k == 0:
    found = True
    print(0)
elif lst_of_scores[k - 1] == lst_of_scores[k]:
    score = lst_of_scores[k - 1]
    for i in range(len(lst_of_scores[:k - 1]), -1, -1):
        n = lst_of_scores[:k][i]
        if n != score:
            found = True
            print(n)
            break
elif lst_of_scores[k - 1] != lst_of_scores[k]:
    found = True
    print(lst_of_scores[k - 1])
if not found:
    print(1)

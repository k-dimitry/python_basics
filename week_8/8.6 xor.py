print(*map(int, map(lambda xy: xy[1] != xy[0], zip(map(int, input().split()), map(int, input().split())))))

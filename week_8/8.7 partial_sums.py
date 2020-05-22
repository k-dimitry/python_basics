from itertools import accumulate
from operator import add

print(*accumulate(map(int, input().split()), add))

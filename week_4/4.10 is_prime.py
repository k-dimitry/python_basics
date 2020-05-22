num = int(input())


def IsPrime(n):
    for i in range(2, n):
        if i > n ** 0.5:
            return True
        if n % i == 0:
            return False
    return True


print("YES" if IsPrime(num) else "NO")

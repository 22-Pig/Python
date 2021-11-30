def isprime(i):
    for k in range(2, i):
        if i % k == 0:
            return False
    return True


m, n = input().split()
m, n = int(m), int(n)
p = [i for i in range(m, n + 1) if isprime(i)]
print(p)
print(len(p), sum(p))

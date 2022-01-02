s = input()
s = tuple(s)
m = s[0]
index = 0
for i in range(1, len(s)):
    if s[i] >= m:
        m = s[i]
        index = i
print('%c   %d' % (m, index))

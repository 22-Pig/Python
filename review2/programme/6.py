a = input()
s = set()
Str = ""
for i in a:
    if (i.isalpha() and (i.lower() not in s)):
        s.add(i.lower())
        Str += i

if (len(Str) >= 10):
    print(Str[0:10])
else:
    print("not found")

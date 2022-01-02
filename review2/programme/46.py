# a = eval(input())
# layer = int(input())
#
#
# def fn(base, deep, layer):
#     if deep == layer:
#         return len([i for i in base if type(i) == int])
#     else:
#         return sum(fn(i, deep + 1, layer) for i in base if type(i) == list)
#
#
# print(fn(a, 1, layer))

a = eval(input())
b = int(input())
out = {}
def fn(base, ceng):
    for i in base:
        if type(i) == int:
            out[ceng] = out.get(ceng, 0) + 1
        else:
            fn(i, ceng + 1)
fn(a, 1)
print(out)
print(out.get(b, 0))



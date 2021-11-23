# %% 求图的顶点数，边数，边的总长  空字典{}，空集合 set()
d = {
    "s": {
        1: 1,
        2: 2,
        3: 4
    },
    1: {
        3: 5
    },
    2: {
        "t": 8,
        3: 78
    },
    3: {
        2: 4,
        "t": 8
    },
    "t": {}
}
v = set()
e = set()
s = 0  # 顶点的集合，边点的集合
for key, value in d.items():
    v.add(key)
    if type(value) == dict:
        for key1, value1 in value.items():
            # 集合不重复
            v.add(key1)
            e.add((key, key1))
            s += value1

print(len(v), len(e), s)

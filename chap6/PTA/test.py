def basic_lis(seq):
    L = [1] * len(seq)
    # seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    # list(enumerate(seasons))
    # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)


L = [49, 64, 17, 100, 86, 66, 68, 68, 87, 96, 19, 99, 35]
print(basic_lis(L))
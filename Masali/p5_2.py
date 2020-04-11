x = [4, 8, 2, 1, 0, 7]
y = [7, 7, 6, 3, 2, 9]

#xy_pairs = list(zip(x, y))

#for xitem, yitem in xy_pairs:
#    pass

for xitem, yitem in zip(x, y):
    print(xitem, '+', yitem, '=', xitem + yitem)

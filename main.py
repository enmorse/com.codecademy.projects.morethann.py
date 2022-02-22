# Write your function here
def more_than_n(lst, item, n):
    return [True if lst.count(item) > n else False]


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

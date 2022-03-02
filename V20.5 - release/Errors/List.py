lst = [0, 1, 2, 3, 4, 5]
print(lst)
def remap_list(lst, idx1, idx2):
    if idx1 == idx2: print("Atributes Error\n"*10)
    ls1 = lst[idx1]
    ls2 = lst[idx2]
    lst[idx2] = ls1
    lst[idx1] = ls2
remap_list(lst, 5, 5)
print(lst)
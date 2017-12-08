l = [11, 3, 6, 4, 9, 34, 70, 45, 20, 36, 50]
def quick(list):
    if list == [] or len(list) == 1:
        return list
    base = list[0]
    left_l, right_l = [], []
    for i in list[1:]:
        if i >= base:
            right_l.append(i)
        else:
            left_l.append(i)
    left_l = quick(left_l)
    right_l = quick(right_l)
    return left_l + [base] + right_l
print (quick(l))
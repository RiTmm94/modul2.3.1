my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while my_list[i] > 0:
    for a in my_list:
        if a < 0:
            break
        if a > 0:
            print(a)
        i = i + 1
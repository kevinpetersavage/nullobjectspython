def sum_list(list):
    sum = None
    if list:
        for i in list:
            if sum == None:
                sum = i
            else:
                sum += i
    return sum

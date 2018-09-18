def sum_list(list):
    sum_of_list = None
    if list:
        for i in list:
            if sum_of_list:
                sum_of_list += i
            else:
                sum_of_list = i
    return sum_of_list


def sum_dict(dictionary):
    sum_of_list = None
    if dictionary:
        for k, v in dictionary.iteritems():
            if sum_of_list:
                sum_of_list += k + v
            else:
                sum_of_list = k + v
    return sum_of_list

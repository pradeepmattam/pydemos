
def binarysearch(sorted_list, number):
    result_index = -1
    if len(sorted_list) == 0:
        return result_index
    l_index = 0
    u_index = len(sorted_list)-1

    while l_index <= u_index:
        m_index = int((l_index + u_index)/2)
        if sorted_list[m_index] < number:
            l_index = m_index + 1
        elif sorted_list[m_index] > number:
            u_index = m_index - 1
        elif sorted_list[m_index] == number:
            result_index = m_index
            break

    return result_index


sorted_list = list(i for i in range(1, 100))
number = 100

if binarysearch(sorted_list, number) != -1:
    print("{} is found in {}".format(number, sorted_list))
else:
    print("{} is not found in {}".format(number, sorted_list))

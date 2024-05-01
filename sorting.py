my_no = [1, 2, 7, 4, 3]
dummy_list = [4, 2, 7, 1, 3]


def selection_sort(your_list):
    """Function to perform selectiom sort

    Args:
        your_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i, num in enumerate(your_list):
        lowest_index = i
        for j in my_no[i + 1:]:
            if j < your_list[lowest_index]:
                lowest_index = j
        if lowest_index != i:
            temp = your_list[i]
            your_list[i] = your_list[lowest_index]
            your_list[lowest_index] = temp
    return your_list


def bubble_sort(your_list):
    """Function to perform bubble sort

    Args:
        your_list (List)

    Returns:
        List
    """
    no_of_times = len(my_no) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(no_of_times):
            if your_list[i] > your_list[i + 1]:
                your_list[i], your_list[i + 1] = your_list[i + 1], your_list[i]
                is_sorted = False
        no_of_times = no_of_times - 1
    return your_list


def insertion_sort(your_list):
    list_length = len(your_list)
    for i in range(1, list_length):
        position = i - 1
        current_item = your_list[i]
        while position >= 0:
            if your_list[position] > current_item:
                your_list[position + 1] = your_list[position]
                position = position - 1
            else:
                break
        your_list[position + 1] = current_item
    return your_list


sorted_list = insertion_sort(my_no)
print(sorted_list)

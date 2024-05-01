def smallest(arr: list[int]):
    smallest_index = 0
    smallest_value = arr[smallest_index]
    for index, value in enumerate(arr):
        if value < smallest_value:
            smallest_value = value
            smallest_index = index

    return [smallest_index, smallest_value]


def selection_sort(arr):
    new_arr = []
    copied_arr = list(arr)
    for i in range(0, len(copied_arr)):
        small = smallest(copied_arr)
        print(small)
        copied_arr.pop(small[0])
        new_arr.append(small[1])

    return new_arr


# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
#     pivot = arr[0]
#     left_side = [i for i in arr[1:] if i < pivot]
#     right_side = [i for i in arr[1:] if i > pivot]

#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)


def total_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + total_sum(arr[1:])


def no_items(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + no_items(arr[1:])


def max_no(arr, max=0):
    if len(arr) == 1:
        if arr[0] > max:
            max = arr[0]
        return max
    else:
        if arr[0] > max:
            max = arr[0]
        print(f"Value for max is {max}")
        return max_no(arr[1:], max)


def quick_sort(items: list[int]) -> list[int]:
    if len(items) < 2:
        return items
    # middle_index = len(items) // 2
    pivot = items[0]
    left_items = [i for i in items[1:] if i < pivot]
    right_items = [i for i in items[1:] if i > pivot]

    return quick_sort(left_items) + [pivot] + quick_sort(right_items)


my_list = [5, 3, 2, 4, 1]
print(total_sum(my_list))
print(f"No of items --> {no_items(my_list)}")
print(f"Max number is {max_no(my_list)}")
print(f"Quick sort --> {quick_sort(my_list)}")

def binary_search(arr: list[int], item: int):
    low = 0
    high = len(arr) - 1

    while low <= high:
        average = (low + high) // 2
        guess = arr[average]
        if item < guess:
            high = average - 1
        if item == guess:
            return average
        if item > guess:
            low = average + 1

    return None


my_list = [1, 2, 3, 4, 5]
result = binary_search(my_list, 1)
print(result)

def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) == 1:
        return arr
    
    middle_point = len(arr) // 2
    first_half = arr[: middle_point]
    second_half = arr[middle_point:]
    
    res = merge(merge_sort(first_half), merge_sort(second_half))
    
    return res

def merge(arr1: list[int], arr2: list[int]):
    sorted_list = []
    
    len_1 = len(arr1)
    len_2 = len(arr2)
    
    long = 0
    short = 0
    
    while long < max(len_1, len_2) and short < min(len_1, len_2):
        if len_1 > len_2:
            if arr1[long] < arr2[short]:
                sorted_list.append(arr1[long])
                long = long + 1
                print(f"current long {long}")
            else:
                sorted_list.append(arr2[short])
                short = short + 1
                print(f"current short {short}")
        else:
            if arr2[long] < arr1[short] :
                sorted_list.append(arr2[long])
                long = long + 1
                print(f"current long {long}")
            else:
                sorted_list.append(arr1[short])
                short = short + 1
                print(f"current short {short}")
    if long != max(len_1, len_2):
        while long != max(len_1, len_2):
            if len_1 > len_2:
                sorted_list.append(arr1[long])
                long = long + 1
            else:
                sorted_list.append(arr2[long])
                long = long + 1
    elif short != min(len_1, len_2):
        while short != min(len_1, len_2):
            if len_2 < len_1:
                sorted_list.append(arr2[short])
                short = short + 1
            else:
                sorted_list.append(arr1[short])
                short = short + 1
    
    return sorted_list
    
    
if __name__ == "__main__":
    b = [4,6]
    a = [1,3,5]
    c = [1,5,4,2,6]
    
    res = merge_sort(c)
    print(f"{res}")
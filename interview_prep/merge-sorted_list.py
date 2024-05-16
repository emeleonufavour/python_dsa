def merge_list(list1: list[int], list2: list[int]):
    pointer_a = 0
    pointer_b = 0
    res = []
    while pointer_a < len(list1) and  pointer_b < len(list2):
        if list1[pointer_a] == list2[pointer_b]:
            res.append(list1[pointer_a])
            res.append(list2[pointer_b])
            pointer_a = pointer_a + 1
            pointer_b = pointer_b + 1
        elif list1[pointer_a] < list2[pointer_b]:
            res.append(list1[pointer_a])
            pointer_a = pointer_a + 1
        elif list1[pointer_a] > list2[pointer_b]:
            res.append(list2[pointer_b])
            pointer_b = pointer_b + 1
            
    while pointer_a < len(list1):
        res.append(list1[pointer_a])
        pointer_a = pointer_a + 1
        
    while pointer_b < len(list2):
        res.append(list2[pointer_b])
        pointer_b = pointer_b + 1
        
    return res


a = [1,2,5]
b = [2,4,6]
answer = merge_list(a, b)
print(answer)
            
             
    
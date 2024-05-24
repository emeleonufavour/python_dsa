def first_uniq_char(s):
    if len(s) == 1:
        return s
    if len(s) == 0:
        return -1
    hash_map = {}
    answer = -1
    
    for letter in s:
        if letter in hash_map:
            hash_map[letter] += 1
        else:
            hash_map[letter] = 1
            
    for index,letter in enumerate(s):
        if hash_map[letter] == 1:
            answer = index
            break
        
    return answer
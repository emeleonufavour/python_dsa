def minWindow(s: str, t: str) -> str:
    # Initialize hash maps to count characters in t and in the current window in s
    t_map = {}
    window_map = {}
    
    for char in t:
        t_map[char] = t_map.get(char, 0) + 1
    
    left_pointer, right_pointer = 0, 0
    formed_chars = 0
    required_chars = len(t_map)
    min_length = float("inf")
    min_window = ""
    
    while right_pointer < len(s):
        char = s[right_pointer]
        window_map[char] = window_map.get(char, 0) + 1
        
        if char in t_map and window_map[char] == t_map[char]:
            formed_chars += 1
        
        while left_pointer <= right_pointer and formed_chars == required_chars:
            char = s[left_pointer]
            
            # Update the minimum window if a smaller valid window is found
            if right_pointer - left_pointer + 1 < min_length:
                min_length = right_pointer - left_pointer + 1
                min_window = s[left_pointer:right_pointer + 1]
            
            window_map[char] -= 1
            if char in t_map and window_map[char] < t_map[char]:
                formed_chars -= 1
            
            left_pointer += 1
        
        right_pointer += 1
    
    return min_window

if __name__ == '__main__':
    
    a = "ADOBECODEBANC"
    b = "ABC"
    answer = minWindow(a, b)
    print(answer)
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        def list_to_int(nums: list[str]) -> int:
            power = 0
            current_index = len(nums) - 1
            integer = 0
            while current_index >= 0:
                digit = int(nums[current_index]) * (10 ** power)
                integer += digit
                power += 1
                current_index -= 1
            return integer

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        s_list = list(s)
        is_negative = False
        reading = False
        result = []
        
        for value in s_list:
            if value == " " and not reading:
                continue
            elif value == " " and reading:
                break
            elif value == "-" and not reading:
                is_negative = True
                reading = True
                continue
            elif value == "+" and not reading:
                reading = True
                continue
            elif value == "-" and reading:
                break
            elif re.fullmatch(r'[A-Za-z]', value):
                break
            elif re.fullmatch(r'\d', value):
                reading = True
                result.append(value)
            else:
                break
        
        if not result:
            return 0

        num = list_to_int(result)
        if is_negative:
            num = -num

        # Clamp the result to the 32-bit signed integer range
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num

            
                
            


if __name__ == "__main__":
    sol = Solution()
    word = " -042"
    result = sol.myAtoi("-91283472332")
    # result = list_to_int([0,4,2])
    # result = list(word)
    # s = "cbbd"
    print(result)
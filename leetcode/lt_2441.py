def is_negative(num: int) -> bool:
    if num < 0:
        return True
    else:
        return False
    
def convert_to_alt(num: int) -> int:
    return num * (-1)

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        hash_map = {}
        highest_value = -1
        if len(nums) == 0 or len(nums) == 1:
            return -1
        for value in nums:
            b = convert_to_alt(value)
            if b in hash_map:
                if is_negative(value):   
                    if b > highest_value:
                        highest_value = b
                else:
                    if value > highest_value:
                        highest_value = value
            else:
                hash_map[value] = True
                continue
        return highest_value


if __name__ == "__main__":
    test = [-30,34,1,32,26,-9,-30,22,-49,29,48,47,38,4,43,12,-1,-8,11,-37,32,40,9,15,-34,-34,-16,-5,26,-44,-36,-13,-16,10,39,-17,-22,17,-16]
    sol = Solution()
    dummy = [-1,10,1,6,7,-7]
    result = sol.findMaxK(test)
    print(result)


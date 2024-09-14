class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        hash_map = {}
        for index,value in enumerate(nums):
            hash_map[index] = value
            
        for i,v in enumerate(nums):
            starting = v
            j = i
            # print(f"starting: {starting}")
            while j < len(nums)-1:
                steps = nums[j]
                # print(f"steps before: {steps} ")
                # print(f"j | {j}, lenght | {len(nums) - 1}, steps | {steps}")
                while j < len(nums) - 1 and steps != 0:
                    if steps > 0:
                        steps  = steps - 1
                        j = j + 1
                    elif steps < 0:
                        steps = steps + 1
                        j = j - 1
                #     print(f"j so far: {j} and lenght: {len(nums)}")
                # print(f"steps after: {steps}")
                if steps != 0 and starting == hash_map[steps - 1]:
                    return True
        return False
            
            
            
        

        
 
if __name__ == "__main__":
    a = 190
    sol = Solution()
    nums = [2,-1,1,2,2]
    res = sol.circularArrayLoop(nums)
    print(res)
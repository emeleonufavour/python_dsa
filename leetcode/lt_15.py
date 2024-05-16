class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i = 0
        j = 1
        k = len(nums) - 1
        result = []
        nums.sort()
        print(f"Sorted ==> {nums}")
        
        if len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
            return []
        
        if len(nums) == 3:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                result.append([nums[i],nums[j],nums[k]])
                return result
            else:
                return []
        
        for index in range(len(nums) - 2):
            i = index
            j = index + 1
            k = len(nums) - 1
            print(f"index => {index}")
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                print(f"Currently looking at => {nums[i]},{nums[j]},{nums[k]}")
                
                if total == 0:
                    if nums[j] == nums[j - 1] and (j - 1) != i:
                        j = j + 1
                    else:
                       print("Total is 0 so we add it")
                       result.append([nums[i],nums[j],nums[k]])
                       j = j + 1
                elif total < 0:
                    i = i + 1
                    j = j + 1
                    print(f"Total({total}) is lesser than 0 so we i:{nums[i]}, j{nums[j]}")
                elif total > 0:
                    k = k - 1
                    print(f"Total({total}) is greater than 0 so we i:{nums[i]}, j{nums[j]}")
                    
        unique_arrays = set(map(tuple, result))
        return list(map(list, unique_arrays))
        
if __name__ == "__main__":
    sol = Solution()
    mylist = [-1,0,1,2,-1,-4]
    answer = sol.threeSum(mylist)
    print(answer)

    
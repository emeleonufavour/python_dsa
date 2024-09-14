class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        nums_len = len(nums)
        
        if nums_len == 0:
            return nums_len

        arrays = 0
        left = 0
        product = 1
        
        for right in range(nums_len):
            product *= nums[right]
            
            if product >= k:
                while left <= right and product >= k:
                    product //= nums[left]
                    left += 1
            
            arrays += right - left + 1
            

        return arrays
        

if __name__ == '__main__':
    sol = Solution()
    nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
    nums2 = [10,5,2,6]
    k = 100
    answer =sol.numSubarrayProductLessThanK(nums2,k)
    print(answer)
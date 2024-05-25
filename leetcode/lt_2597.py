class Solution:
    def is_beautiful(self, nums: list[int], k: int):
        hash_map = {}
        for index,value in enumerate(nums):
            difference1 = value - k
            difference2 = value + k
            if (difference1 in hash_map) or (difference2 in hash_map) :
                return False
            else:
                hash_map[value] = index
        return True
            
    
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                if self.is_beautiful(subset.copy(), k) and len(subset.copy()) != 0:
                    res.append(subset.copy())
                return
                
            subset.append(nums[i])
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return len(res)

if __name__ == "__main__":
    sol = Solution()
    a = [2,4,6]
    k = 2
    result = sol.beautifulSubsets(a, k)
    answer = sol.is_beautiful(a,2)
    print(result)
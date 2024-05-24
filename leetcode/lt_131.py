class Solution:
    def isPali(self, s:str, l:int, r:int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        
        
    def partition(self,s:str) -> list[list[str]]:
        res = []
        partition = []
        
        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        dfs(0)
        return res
        
        
        
                    
if __name__ == "__main__":
    sol = Solution()
    word = "aab"
    answer = sol.partition(word)
    sub = word[0:1]
    
    print(answer)
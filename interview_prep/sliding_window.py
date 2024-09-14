class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        window_len = 10
        s_len = len(s)
        
        if s_len <= window_len:
            return []
        hash_maps = set()
        left = 0
        hash_map = {}
        res = []
        for i in range(s_len):
            if s[i] not in hash_map:
               hash_map[s[i]]  = 0
            else:
                hash_map[s[i]] += 1
                
            if (i - left + 1) > 10:
                if s[left] in hash_map:
                    hash_map[s[left]] -= 1
                    if hash_map[s[left]] == 0:
                        del hash_map[s[left]]
                left += 1
                

            if (i - left + 1) == window_len:
                print(f"left is: {left}")
                sorted_map = tuple(sorted(hash_map))
                if sorted_map in hash_maps:
                    
                   print(f"adding for left: {left}")
                   res.append(s[left:i + 1])
                   hash_maps.remove(tuple(sorted(hash_map)))
                else:
                    hash_maps.add(tuple(sorted_map))
        return res
            
    
                
            
if __name__ == '__main__':
    sol = Solution()
    s ="aaabb"
    b = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    t = [-1,0,1,2,-1,-4]
    # answer = sol.findRepeatedDnaSequences(b)
    # answer =helper( s,t)
    print(s.split("b"))
    
def longestSubstring(self, s, k):
    for c in set(s):
        if s.count(c) < k:
            return max(self.longestSubstring(t, k) for t in s.split(c))
    return len(s)
        
        
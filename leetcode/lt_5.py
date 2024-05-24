def is_palindrome(w: str):
    if len(w) <= 1:
        return True
    
    if w[0] != w[-1]:
        return False
    
    return is_palindrome(w[1:-1])

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0:
            return s
        max_string = ""
        for index,value in enumerate(s):
            for index2,value2 in enumerate(s[index+1:]):
                print(f"Looking at {s[index + 1:]}")
                if value == value2:
                    print(f"Found {value},{index} and {value2},{index2} to be equal")
                    word = s[index:(index + index2 + 2)]
                    print(f"Word => {word}")
                    res = is_palindrome(word)
                    
                    if res and len(word) > len(max_string):
                        max_string = word
                        break
        return max_string
                    
        
        


if __name__ == "__main__":
    sol = Solution()
    mylist = [-1,0,1,2,-1,-4]
    # result = is_palindrome("aca")
    result = sol.longestPalindrome("babad")
    # s = "cbbd"
    print(result)
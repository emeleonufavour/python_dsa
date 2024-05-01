class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        if len(word_list) == 0:
            return 0
        return len(word_list[-1])


if __name__ == "__main__":
    sol = Solution()
    count = sol.lengthOfLastWord("luffy is still joyboy")
    print(count)

def reverse_string(string :str):
    """Function to reverse a string"""
    string_length = len(string)
    if string_length == 1:
        return string
    else:
        return string[-1] + reverse_string(string[:(string_length-1)]) 
    
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if len(word) == 0:
            return ""
        if len(word) == 1:
            return word
        prefix = ""
        new_word = ""
        for index,value in enumerate(word):
            if value == ch:
                prefix = word[:index+1]
                new_word = word[index+1:]
                break
        if prefix == "" and new_word == "":
            return  word
        else:
            return reverse_string(prefix) + new_word
            
  
word = "abced"
# last = word[-1]
# new = word[:2+1]
# new_2 = word[2+1:]
# print(f"last: {last}, new: {new}, new 2: {new_2}")

if __name__ == "__main__":
    sol = Solution()
    result = sol.reversePrefix(word, "z")
    print(result)


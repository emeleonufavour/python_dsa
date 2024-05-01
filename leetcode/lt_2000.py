def reverse_string(string :str):
    """Function to reverse a string"""
    string_length = len(string)
    if string_length == 1:
        return string
    else:
        return string[-1] + reverse_string(string[:(string_length-1)]) 
    
# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         prefix = ""
#         for index,value in enumerate(word):
#             if value == ch:
#                 prefix = word[:index]
                
            
  
word = "abced"
last = word[-1]
new = word[:2+1]
print(f"last: {last}, new: {new}")


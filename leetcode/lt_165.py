def convert_to_list(string: str) -> list[int]:
    integer_list = [int(x) for x in string.split(".")]
    return integer_list

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list_1 = convert_to_list(version1)
        list_2 = convert_to_list(version2)
        len1 = len(list_1)
        len2 = len(list_2)
        
        if len1 == 0 and len2 != 0:
            return -1
        if len1 != 0 and len2 == 0:
            return 1
        if len1 == 0 and len2 == 0:
            return 0
        result = 0
        i = 0
        if len2 > len1:
            while i < len2:
                value_2 = list_2[i]
                if i < len1:
                    value_1 = list_1[i]
                    if value_1 > value_2:
                        result = 1
                        break
                    elif value_1 < value_2:
                        result = -1
                        break
                else:
                    if value_2 > 0:
                        return -1
                i = i + 1
        else:
            while i < len1:
                value_1 = list_1[i]
                if i < len2:
                    value_2 = list_2[i]
                    if value_2 > value_1:
                        result = -1
                        break
                    elif value_2 < value_1:
                        result = 1
                        break
                else:
                    if value_1 > 0:
                        return 1
                i = i + 1
        return result

    
if __name__ == "__main__":
    sol = Solution()
    result = sol.compareVersion("1.0.2","1")
    a = "1.1"
    # result = convert_to_list(a)
    print(result)
    # count = 0
    # while count < 5:
    #     count = count + 1
    #     print(count)
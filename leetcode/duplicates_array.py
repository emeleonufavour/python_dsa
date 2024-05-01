nums = [4, 3, 2, 7, 8, 2, 3, 1]


def find_duplicates(array_list: list[int]) -> list[int]:
    """Find duplicates in an array"""
    if (len(array_list) == 0):
        return []
    if (len(array_list) == 1):
        return array_list
    hash_map = {}
    duplicates_set = set()
    for item in array_list:
        if item in hash_map:
            duplicates_set.add(item)
        else:
            hash_map[item] = True

    return list(duplicates_set)


print(find_duplicates(nums))


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:

        if (len(nums) == 1 or len(nums) == 0):
            return []
        hash_map = {}
        duplicates_set = set()
        for item in nums:
            if item in hash_map:
                duplicates_set.add(item)
            else:
                hash_map[item] = True

        return list(duplicates_set)

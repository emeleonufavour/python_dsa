my_list = [1, 2, 1, 2, 3]


class Solution:

    def subarraysWithKDistinct(self, array: list[int], k: int) -> int:
        """Function to find maximum possible good sub arrays from an array"""

        # Returns 0 is the array is empty or 1 if the array length is 1.
        if len(array) == 0:
            return 0
        if len(array) == 1:
            return 1

        # Keeps track of amount of good sub arrays so far
        count = 0

        # The scope of the current sub array we are looking at.
        sub_array = []

        # Keeps track of different values we have seen so far
        hash_map = {}

        # Key to know length of Hash map so far. To provide an O(1) lookup for the length.
        hash_map['length'] = 0

        # Two pointers
        a = 0
        b = 0

        # We perform the loop while the first pointer has not reached the end
        while a < len(array):

            # We check the different integers in the sub array so far
            different_integers = hash_map['length']

            # If the second pointer has reached the end, we increment
            # the first pointer by 1 and start again from the first pointer
            if b == len(array):
                if k == different_integers:

                    count += 1

                sub_array = []
                hash_map = {}
                hash_map['length'] = 0
                a += 1
                b = a

            # If the different integers is more than intended. We start again.
            elif different_integers > k:
                sub_array = []
                hash_map = {}
                hash_map['length'] = 0
                a += 1
                b = a
            else:
                if k == different_integers:

                    count += 1

                sub_array.append(array[b])
                if array[b] not in hash_map:
                    hash_map[array[b]] = 1
                    hash_map['length'] = hash_map.get('length', 0) + 1
                else:
                    hash_map[array[b]] = hash_map.get(array[b]) + 1

                b += 1

        return count

# class Solution:

#     def subarraysWithKDistinct(self, array: list[int], k: int) -> int:
#         def count_subarrays_with_k_distinct(arr: list[int], k: int) -> int:
#             count = 0
#             left, right = 0, 0
#             window = {}
#             while right < len(arr):
#                 window[arr[right]] = window.get(arr[right], 0) + 1

#                 while len(window) > k:
#                     window[arr[left]] -= 1
#                     if window[arr[left]] == 0:
#                         del window[arr[left]]
#                     left += 1

#                 count += right - left + 1  # Add the count of valid subarrays
#                 right += 1

#             return count

#         return count_subarrays_with_k_distinct(array, k) - count_subarrays_with_k_distinct(array, k - 1)


if __name__ == "__main__":
    sol = Solution()
    result = sol.subarraysWithKDistinct(my_list, 2)
    print(result)

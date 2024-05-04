def quick_sort(arr)-> list:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
    
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
    
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
    
        return boats


              
if __name__ == "__main__":
    sol = Solution()
    result = sol.numRescueBoats([5,1,4,2], 6)
    print(result)

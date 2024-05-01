

def countdown(n):
    """Countdown from n recursively"""
    if n == 0:
        return

    print(n)
    countdown(n - 1)


def count_x(array):
    """This function finds all the x that occurs in an array"""
    if len(array) == 1:
        if array[0] == "x":
            return 1
        else:
            return 0

    if array[0] == "x":
        return 1 + count_x(array[1:])
    else:
        return count_x(array[1:])


def factorial(n):
    """Calculate a factorial recursively"""
    if n == 1:
        return 1
    return n * factorial(n-1)


def print_every_other(low, high):
    """Print numbers from low to high in 2 steps"""
    if low > high:
        return
    if low <= high:
        print(low)
        print_every_other(low=low + 2, high=high)


dummy_array = [1, 2, 3,
               [4, 5, 6],
               7,
               [8,
                [9, 10, 11,
                 [12, 13, 14]
                 ]],
               [15, 16, 17, 18, 19,
                [20, 21, 22,
                 [23, 24, 25,
                  [26, 27, 29]
                  ], 30, 31], 32
                ], 33]

xs = list("xbxcxd")


def print_elements_array(your_array):
    """Print all numbers in array"""
    for i in your_array:
        if isinstance(i, list):
            print_elements_array(i)
        else:
            print(i)


# def permute(str, remaining):
#     """Generate a permutation for a str recursively"""
#     if remaining == "":
#         print(str)
#     for index, c in enumerate(remaining):
#         print(f"""The string is {str} and We are currently looking at {c} in {
#               remaining}. The index is {index}""")
#         new_str = str + c
#         print(f"The new string is {new_str}")
#         new_remaining = remaining[0:index] + remaining[index+1:]
#         print(f"The new remainder is {new_remaining}")
#         permute(new_str, new_remaining)

def permute(str, remaining):
    """Generate a permutation for a str recursively"""
    permutations = []

    if remaining == "":
        permutations.append(str)
    for index, c in enumerate(remaining):
        new_str = str + c
        new_remaining = remaining[0:index] + remaining[index+1:]
        permutations.extend(permute(new_str, new_remaining))

    return permutations


# def permute(items: list[int], variation: list[int], result:  list[list[int]]):
#     """Generate a permutation for a str recursively"""
#     if len(items) == 0:
#         result.append(variation.copy())

#     for index, item in enumerate(items):
#         new_variation = variation.copy()
#         new_variation.append(item)

#         remainder = items[0:index] + items[index+1:]
#         permute(items=remainder, variation=new_variation,  result=result)

#     return result


# def permute(items: list[int], variation: list[int], result: list[list[int]]):
#     """Generate permutations recursively"""
#     if len(items) == 0:
#         # Use a copy of the variation to avoid modifying the original list
#         result.append(variation.copy())
#         print(f"We are adding this variation {variation} to the result")
#         print(f"""The result so far is {
#               result} and the variation should be empty ==> {variation}""")

#     for index, item in enumerate(items):
#         print(f"The variation so far is {variation} and We are currently looking at {item} in "
#               f"{items}. The index is {index}")

#         # Create a new copy of the variation for each recursive call
#         new_variation = variation.copy()
#         new_variation.append(item)

#         print(f"The new variation is {new_variation}")

#         remainder = items[:index] + items[index+1:]
#         print(f"The new remainder is {remainder}")

#         # Make a recursive call with the new_variation
#         permute(items=remainder, variation=new_variation, result=result)


# counts = count_x(xs)
# print(f"Counts ==> {counts}")
# result = permute(items=[1, 2, 3], variation=[], result=[])
# print(result)

# result = permute("", "abc")
# print(result)

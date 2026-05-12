from typing import List
import copy


# lambdas (your style)
key = lambda x: x          # alphabetical comparison
key2 = lambda x: abs(x)    # absolute value comparison


def sort_words(words: List[str]) -> List[str]:
    new = copy.deepcopy(words)
    n = len(new)

    for i in range(n):
        for j in range(0, n - i - 1):

            # alphabetical ASCENDING (A → Z)
            if key(new[j]) > key(new[j + 1]):
                new[j], new[j + 1] = new[j + 1], new[j]

    return new


def sort_numbers(numbers: List[int]) -> List[int]:
    new_number = copy.deepcopy(numbers)
    n = len(new_number)

    for i in range(n):
        for j in range(0, n - i - 1):

            # absolute value DESCENDING (biggest first)
            if key2(new_number[j]) < key2(new_number[j + 1]):
                new_number[j], new_number[j + 1] = new_number[j + 1], new_number[j]

    return new_number


# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))

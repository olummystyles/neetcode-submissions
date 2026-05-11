from typing import List


# Bubble Sort for words
def sort_words(words: List[str]) -> List[str]:
    n = len(words)

    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]

    return words


# Bubble Sort for integers
def sort_numbers(numbers: List[int]) -> List[int]:
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


# Bubble Sort for decimal numbers
def sort_decimals(numbers: List[float]) -> List[float]:
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))

from typing import List


def sort_words(words: List[str]) -> List[str]:
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j] < words[j + 1]:
                words[j], words[j + 1] =words[j + 1], words[j]
    return words

def sort_numbers(items: List[int]) -> List[int]:
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j] < items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def sort_decimals(items: List[float]) -> List[float]:
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j] < items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))

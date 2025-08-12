# 1. Unique Elements Function

def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(unique_elements([1, 2, 2, 3, 4, 1, 5]))  

# 2. List Rotation

def rotate_list(lst, k):
    k = k % len(lst) 
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2))  

# 3. Find Longest Word

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("Python is an amazing programming language"))  


# 4. Sum of Digits Function

def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))  

print(sum_of_digits(12345))  

# 5. Character Frequency Counter

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("hello"))
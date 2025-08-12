# 1. Numbers Divisible by 3 or 5

for i in range(1, 101):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        print(i, end=" ")

for i in range(1, 16):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        print(i, end=" ")
        
# 2. Reverse Words in a Sentence

sentence = "Python is fun"
word = ""
words = []

for char in sentence:
    if char == " ":
        words.append(word)
        word = ""
    else:
        word += char
words.append(word)


reversed_sentence = ""
for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i]
    if i != 0:
        reversed_sentence += " "

print(reversed_sentence)


# 3. Star Diamond Pattern

n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    
# 4. Count Consonants in a String

string = "hello world"
count = 0
vowels = "aeiouAEIOU"

for char in string:
    if char.isalpha() and char not in vowels:
        count += 1

print(count)  


# 5. Number Guessing Game

secret_number = 8

while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong, try again.")


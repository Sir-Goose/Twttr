vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

long_tweet = input("Input: ")

for letter in long_tweet:
    for vowel in vowels:
        if letter == vowel:
            long_tweet = long_tweet.replace(letter, "")

print(long_tweet)





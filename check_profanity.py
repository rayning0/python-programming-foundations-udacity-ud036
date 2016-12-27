import os
from profanity import profanity

quotes = open(os.getcwd() + '/movie_quotes.txt', 'r')
file_text = quotes.read()
print(file_text)

if profanity.contains_profanity(file_text):
    print("\nHas bad words. Censored version:\n")
    print(profanity.censor(file_text))
else:
    print("\nIt's clean\n")

quotes.close()

# Print number to words 

# Exp. 123 => one two three

# import lib.

import inflect

num = inflect.engine()

words = num.number_to_words(1234)
print(words)

words = num.number_to_words(num.ordinal(1234))        # ordinal
print(words)

# Thanks for Watching

# def is_pangram(sentence):
#     alphabet_list= []
#     for letter in sentence:
#         if letter not in alphabet_list:
#             alphabet_list.append(letter)

#     return len(alphabet_list) >= 26


# better soluion

import string

def is_pangram(sentence):
    return set(sentence.lower()) >= set(string.ascii_lowercase)

print(is_pangram('This is a boy'))
print(is_pangram('The quick, brown fox jumps over the lazy dog!'))
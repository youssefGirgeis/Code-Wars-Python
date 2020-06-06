# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. 
# For example:
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false

# Write a function that will find all the anagrams of a word from a list. You will be given two inputs 
# a word and an array with words. You should return an array of all the anagrams or 
# an empty array if there are none. For example:

#solution

def anagrams(word, words):
    
    anagrams_list = []
    for w in words:

        if ''.join(sorted(word)) == ''.join(sorted(w)):
            anagrams_list.append(w)

    return anagrams_list


# tesing

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
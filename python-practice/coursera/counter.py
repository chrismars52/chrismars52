handle = open("ipsum.txt")
text = handle.read()
counter = dict()
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for word in text.split():
    if word in uninteresting_words : continue
    if word[len(word)-2:] == "'s":
        counter[word] = counter.get(word, 0) + 1
        continue
    new_word =""
    for char in word:
        if char not in punctuations : new_word += char
    counter[new_word] = counter.get(new_word, 0) + 1

bigword = None
bigcount = None
for key,val in counter.items():
    #if val == 1 : print("The word -{}- occurs {} time".format(key,val))
    #else : print("The word -{}- occurs {} times".format(key,val))
    if bigcount == None or bigcount < val:
        bigcount = val
        bigword = key
print('"{}" is the most used word with {} appearances.'.format(bigword, bigcount))
print()
print()
print( sorted( [ (v,k) for k,v in counter.items() ], reverse=True ) )

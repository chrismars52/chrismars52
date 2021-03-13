handle = open("colossians1.txt")
text = handle.read()
counter = dict()

no_punc = ""

for char in text:
    if char not in ",.;:" : no_punc = no_punc + char

for word in no_punc.split():
    counter[word] = counter.get(word, 0) + 1

bigword = None
bigcount = None
revlist = list()
for key,val in counter.items():
    revlist.append((val,key))
    if bigcount == None or bigcount < val:
        bigcount = val
        bigword = key
print("{} is the most used word with {} appearances.".format(bigword, bigcount))
print(revlist)
lst = sorted(revlist, reverse=True)
for val, key in lst[:10] : print(key, val)

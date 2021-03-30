import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
print()
print()
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().split())
    words = line.decode().split()
    for word in words:
        if 'http' in word :
            new_fhand = urllib.request.urlopen(word[word.find("http"):word.find(".htm")+4])
            for new_line in new_fhand:
                print(new_line.decode().split())

import re
sumFile = open('C:/Users/Chris/github/chrismars52/python-practice/severance/regex_sum_1191518.txt', 'r')
sumText = sumFile.readlines()
sum = 0
for line in sumText:
    for num in re.findall('[0-9]+',line) : sum += int(num)
print(sum)

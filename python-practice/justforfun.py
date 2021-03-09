def convert_ascii(num):
    print("For number: " + str(num))
    chars = [128,64,32,16,8,4,2,1]
    bin = [0,0,0,0,0,0,0,0]
    for i in range(8):
        if num // chars[i] >= 1:
            bin[i] = 1
            num = num - chars[i]
    print(bin)

convert_ascii(115)
print
print
convert_ascii(75)
print
print
convert_ascii(46)
print
print
convert_ascii(4)
print
print
convert_ascii(47)
print
print
convert_ascii(9)
print
print
convert_ascii(41)
print
print
convert_ascii(100)
print
print
convert_ascii(53)
print
print
convert_ascii(116)
print
print

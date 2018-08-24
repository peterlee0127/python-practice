#This problem was asked by Amazon.

#Run-length encoding is a fast and simple method of encoding strings. 
#The basic idea is to represent repeated successive characters as a single count and character. 
#For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

#Implement run-length encoding and decoding. 
#You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
#You can assume the string to be decoded is valid.


def encode(string):
    print("input:"+string)
    result = ""
    temp = []
    for index,char in enumerate(string):
        count = len(temp)
        if count > 0 and temp[count-1] != char:
            result = result + str(count) + temp[count-1]
            temp = []
        temp.append(char)
        if index == len(string)-1:
            count = len(temp)
            result = result + str(count) + temp[count-1]
            


    return result


print(encode("AAAABBBCCDAA"))
print(encode("AABBBA"))

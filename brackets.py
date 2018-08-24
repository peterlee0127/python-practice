#This problem was asked by Facebook.

#Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

#For example, given the string "([])[]({})", you should return true.

#Given the string "([)]" or "((()", you should return false.



def parseBrackets(string):
    temp = []
    print(string)
    for index,char in enumerate(string):
        if char == "[" or char == "(" or char == "{":
            temp.append(char)
        elif len(temp) > 0:
            last = temp[len(temp)-1]
            if char == "}" and last == '{':
                temp.pop()
            if char == "]" and last == '[':
                temp.pop()
            if char == ")" and last == '(':
                temp.pop()
    if index == len(string)-1:
        if len(temp) == 0:
            return True
        else:
            return False





print(parseBrackets("([])[]({})")) # true
print(parseBrackets("{[()]}"))  # true
print(parseBrackets("{[(])}")) # false
print(parseBrackets("{{[[(())]]}}")) # true

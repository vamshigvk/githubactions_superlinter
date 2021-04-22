# Python program to find all string which are greater than given length k, function find string greater than length k
def string_k(k, str):
    # create the empty string
    string = []
    text = str.split(" ")
    for x in text:
        # if length of current sub string
        # is greater than k then
        if len(x) > k:
            # append this sub string in
            # string list
            str1=string.append(x)
    return str1


k = 3
str = "geek for geeks"
print(string_k(k, str))

# string compression
# implement a method to perform basic string compression using the counts of
# repeated characters. for example, the string aabcccccaaa would become a2b1c5a3.
# if the "compressed" string would not become smaller than the original string,
# your method should return the original string. you can assume the string has
# only uppercase and lowercase letters (a-z).

def string_compress(str):

    if str == "":
        print "str empty"
        return
    hashmap = {}
    start_char = str[0]
    char_count = 0
    result = ""
    for i in xrange(len(str)):
        if not str[i].isalpha():
            print "invalid char"
            return
        if str[i] == start_char:
            char_count += 1
        else:
            result = "{0}{1}{2}".format(result, start_char, char_count)
            char_count = 1
            start_char = str[i]
    result = "{0}{1}{2}".format(result, start_char, char_count)
    print result


string_compress("aabcccccaaa")
string_compress("abcd")
string_compress("AAAaaBccccDDDaaaa")
string_compress("")
string_compress("^^^^^%%^!")
string_compress("a sdf asf  ")

#one away: there are three types of edits that can be performed on strings:
#   insert a character, remove a character, or replace a character. Given two
#   strings, write a function to check if they are one edit (or zero edits) away.

def oneAway(str1, str2):
    print "oneAway({0}, {1})".format(str1, str2)
    hashmap = {}
    if len(str1) + 1 != len(str2) or len(str1) - 1 != len(str2) or len(str1) != len(str2):
        print len(str1)
        print len(str2)
    else:
        return False
    if len(str1) > len(str2):
        bigStr = str1
        smallStr = str2
    else:
        bigStr = str2
        smallStr = str1
    for i in bigStr:
        hashmap[i] = 0
    return True

print oneAway("pale", "ple")
print oneAway("pales", "pale")
print oneAway("pale", "bale")
print oneAway("pale", "bae")

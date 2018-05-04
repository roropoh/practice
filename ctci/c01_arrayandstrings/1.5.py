#one away: there are three types of edits that can be performed on strings:
#   insert a character, remove a character, or replace a character. Given two
#   strings, write a function to check if they are one edit (or zero edits) away.

def oneAway(str1, str2):
    len_diff = abs(len(str1) - len(str2))
    if len_diff > 1:
        return False
    elif len_diff == 0:
        difference_count = 0
        for i in xrange(len(str1)):
            if str1[i] != str2[i]:
                difference_count += 1
                if difference_count > 1:
                    return False
            return True
    else:
        if len(str1) > len(str2):
            long, short = str1, str2
        else:
            long, short = str2, str1
        for i in xrange(len(short)):
            if short[i] not in long:
                return False
        return True

print oneAway("pale", "ple")
print oneAway("pales", "pale")
print oneAway("pale", "bale")
print oneAway("pale", "bae")

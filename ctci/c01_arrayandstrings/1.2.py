def perm(str1, str2):
    print "perm({0}, {1})".format(str1, str2)
    if len(str1) != len(str2):
        return False
    hashmap = {}
    for i in str1:
        hashmap[i] = True
    for i in str2:
        try:
            hashmap[i]
        except:
            return False
    return True

print perm("abcd", "dcba")
print perm("aaaaa", "bbbb")
print perm("aaaaa", "aaa")

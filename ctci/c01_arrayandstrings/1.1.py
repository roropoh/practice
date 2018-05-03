def is_unique(str):
    print "is_unique({0})".format(str)
    hashmap = {}
    for i in str:
        try:
            hashmap[i]
            return False
        except:
            hashmap[i] = True
    return True

print is_unique("aaaaaa")
print is_unique("abcd")
print is_unique("abababa")
print is_unique("")

def palindrome(str):
    print "palindrome({0})".format(str)
    table = getCountPerCharacter(str)
    return checkMaxOneOddinTable(table)

def checkMaxOneOddinTable(table):
    foundOdd = False
    for i in table:
        if table[i] % 2 == 1:
            if foundOdd == True:
                return False
            foundOdd = True
    return True

def getCountPerCharacter(str):
    hashmap = {}
    for i in str:
        if i.isalpha():
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
    return hashmap

print palindrome("pale, ple")
print palindrome("pales, pale")
print palindrome("pale, bale")
print palindrome("pale, bae")

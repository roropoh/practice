# Experiments using Python arrays and vectors

def array_test():
    ar = [3, 2, 4, 5, 10, 16, 22, 1]
    print "original ar:",ar
    print "len(ar):",len(ar)

    ar.append(6)
    print ar
    print "len(ar):",len(ar)

    pos = 4
    print "Index of ",pos,": ",ar.index(pos)
    print "Value at the index of ",ar.index(pos),":",ar[ar.index(pos)]

    ar.remove(4)  # remove the first occurence of item with given value
    print("Removed 4: ", ar)
    print "len(ar):",len(ar)

    ar.reverse()
    print("reversed: ", ar)
    print("sorted return: ", sorted(ar))

    ar.sort()
    print("sorted in place: ", ar)
    print "len(ar):",len(ar)

    ar2 = []
    print len(ar2)
    print is_empty(ar2)

def is_empty(ar):
    if len(ar) > 0:
        return False
    return True

def main():
    array_test()

if __name__ == "__main__":
    main()

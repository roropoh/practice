def URLify(str, strlen):
    print "URLify({0}, {1})".format(str, strlen)
    newstr = ""
    for i in str[:strlen]:
        if i == " ":
            newstr += "%20"
        else:
            newstr += i
    return newstr

print URLify("Mr John Smith   ", 13)

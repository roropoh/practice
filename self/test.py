def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print count_bits(10)


# Initializing dictionary
dic = { 'Name' : 'Nandini', 'Age' : 19, 'ID' : 2541997 }

# Initializing list
li = [ 1, 3, 5, 6 ]

# using type() to display data type
# print ("The data type of dic is : ")
# print (type(dic))
#
# print ("The data type of li is : ")
# print (type(li))

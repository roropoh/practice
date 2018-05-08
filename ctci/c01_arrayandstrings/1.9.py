# 1.9 String Rotation: Assume you have a method i 5 S u b s t r i n g which
# checks ifone word is a substring of another. Given two strings, 51 and 52,
# write code to check if s2 is a rotation of s1 using only one call to
# isSubstring (e.g., "waterbottle" a rotation "erbottlewat").

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1s1 = s1 + s1
    if s2 in s1s1:
        return True
    return False

print string_rotation("waterbottle", "erbottlewat")

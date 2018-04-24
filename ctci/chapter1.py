def unique_chars(str_input):
  print("unique_chars" + "(" + str_input + ")")
  hashmap = {}
  for i in str_input:
    if i in hashmap:
      return False
    hashmap[i] = True
  return True

def dup_chars(str_input):
  print("dup_chars()")
  hashmap = {}
  result_string = ""
  for i in str_input:
    if i not in hashmap:
      result_string += i
    hashmap[i] = True
  return result_string

def is_anagram(str_input_1, str_input_2):
  print("is_anagram({0}, {1})".format(str_input_1, str_input_2))
  hashmap = {}
  if len(str_input_1) is not len (str_input_2):
    return False
  for i in str_input_1:
    hashmap[i] = True
  for i in str_input_2:
    if i not in hashmap:
      return False
  return True

def replace_str(str_input, char):
  print("replace all spaces with [{0}] in [{1}]".format(char, str_input))
  result_string = ""
  for i in str_input:
    if i is " ":
      result_string+="%20"
    else:
      result_string+=i
  return result_string

def isSbustring(str1, str2):
  if len(str1) is not len(str2):
    return False
  s = str1 + str1
  if str2 in s:
    return True
  return False

def question1_1():
  print("1.1 - determine if a string has all unique characters")
  result = unique_chars("designer")
  print(result)
  result = unique_chars("uncopyrightable")
  print(result)

def question1_2():
  print("1.2 - reverse a C-Style String, abcd reverse including null character")
  original = "abcde\0"
  finish_correct = "edcba\0"
  answer = original[:-1]
  answer = answer[::-1]
  print("Before adding null: ")
  print(answer == finish_correct)
  answer = answer + "\0"
  print("After adding null: ")
  print(answer == finish_correct)

def question1_3():
  print("1.3 - remove dup chars in string")
  test1_original = "aaronaa"
  test1_finish_correct = "aron"
  answer1 = dup_chars(test1_original)
  print(answer1 == test1_finish_correct)
  #test cases
  # string with dup characters - "aaaa"
  # string without dup chars - "abcd"
  # empty string
  # continuous repeating chars - "aaaabbbb"
  # non-continuous repeating chars - "abababab"

def question1_4():
  print("1.4 - if two strings are anagrams or not")
  print(is_anagram("elbow", "below"))
  print(is_anagram("elbow", "happy"))

def question1_5():
  print("1.5 - replace all spaces in a string with '%20'")
  print(replace_str("Hello, I am a robot.", "%20"))

def question1_8():
  print("1.8 - given 2 strings, is s2 a rotation of s1")
  print(isSbustring("waterbottle", "erbottlewat"))

def main():
  # question1_1()
  # question1_2()
  # question1_3()
  # question1_4()
  # question1_5()
  question1_8()

if __name__== "__main__":
  main()

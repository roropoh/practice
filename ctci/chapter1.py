def unique_chars(str_input):
  print("unique_chars" + "(" + str_input + ")")
  hashmap = {}
  for i in str_input:
    if i in hashmap:
      return False
    hashmap[i] = True
  return True

def question1_1():
  print("1.1 - determine if a string has all unique characters")
  results = unique_chars("designer")
  print(results)
  results = unique_chars("uncopyrightable")
  print(results)

def question1_2():
  print("1.2 -reverse a C-Style String, abcd reverse including null character")
  


def main():
  print("start chapter1.py")
  question1_1()
  question1_2()


  print("end chapter1.py")

if __name__== "__main__":
  main()

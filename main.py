def main(): 
  book_path = "./books/frankenstein.txt"
  text = read_book(book_path)
  word_count = count_words(text)
  letter_count = count_letters(text)
  letter_count_list = sort_letter_count(letter_count)

  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document\n")
  for item in letter_count_list:
    print(f"The '{item["letter"]}' character was found {item["num"]} times")
  print("--- End report ---")

def read_book(book):
  with open(book) as f:
    return f.read()

def count_words(book_words):
  return len(book_words.split())

def count_letters(book_words):
  letter_dict = {}
  book_characters = book_words.lower()
  for character in book_characters:
    if character in letter_dict:
      letter_dict[character] += 1
    elif character.isalpha():
      letter_dict[character] = 1
  return letter_dict

def sort_on(dict):
  return dict["num"]

def sort_letter_count(letter_dict):
  letter_list = []
  for letter in letter_dict:
    letter_list.append({"letter":letter, "num":letter_dict[letter]})
  letter_list.sort(reverse=True,key=sort_on)
  return letter_list

main()
#Bài 1: Đảo ngược chuỗi trong python
def convert_string(s):
    list_str= s.split(" ")
    list_str.reverse()
    str = " ".join(list_str)
    new_str = ''
    for i in str:
        if i.isupper(): new_str += i.lower()
        elif i.islower(): new_str += i.upper()
        else: new_str += i
    return new_str

s = "tHE fOX iS cOMING fOR tHE cHICKEN"
print(convert_string (s) ) 

#Bài 2: Sorting - Sắp xếp điểm thi
def sort_list_last(list_a):
  list_sorted = sorted(list_a, key=lambda tup:tup[2])
  return list_sorted

A = [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]
print("Danh sách sau khi sắp xếp: ", sort_list_last(A))


#Bài 3: Bài tập tổng hợp phần Basic - Đếm từ
import sys

# Đếm từ
def print_words(filename):
    words_count = readfile_count_words(filename)
    words_count_sorted =  sorted(list(words_count), key = lambda k: k[0])
    for i in words_count_sorted:
        print (i, ":", words_count[i])

def print_top(filename):
    words_count = readfile_count_words(filename)
    words_count_sorted =  sorted(list(words_count), key = words_count.get, reverse = True)
    inc = 1
    for i in words_count_sorted:
        print (f"{inc}. {i}: {words_count[i]}")
        inc += 1
        if inc > 20: break

def readfile_count_words(filename):
    f =  open(filename, encoding='utf-8-sig')
    content = remove_special_char(f.read())
    list_str = content.split(" ")
    dict_count = {}
    for i in list_str:
        if i == '': continue
        i = i.lower()
        if i in dict_count: dict_count[i] += 1
        else: dict_count[i] = 1

    return dict_count
def remove_special_char(str):
    special_char = ['.', ',', '?', '!', '\n', '\r', '(', ')', '[', ']', ':', '--', ';', '`', "' ", '"']
    for j in special_char:
        str = str.replace(j, " ")
    return str
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()


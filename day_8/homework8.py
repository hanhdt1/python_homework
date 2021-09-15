#Bài 3: Regex - ApacheLog
import sys
import re

def readfile_regex_image(filename):
    f =  open(filename, encoding='utf-8-sig')
    content = f.read()
    data_find = re.findall("GET (.*\.jpg)", content, re.MULTILINE)
    if(data_find):
        domain = get_domain(filename)
        #loại bỏ image trùng
        data = set(data_find) 
        inc = 1;
        print ("Danh sách ảnh trong file: ")
        for path in data:
            print(f"{inc}. {domain}{path}")
            inc += 1
    else:
        print ("Không có link ảnh trong file")        

    
def get_domain(filename):
    #regex như này thì đuôi file là google.com.vn vẫn hiểu được
    re_host = re.search("[\.](\w*(\.[a-z]{2,6}){1,2})$", filename) 
    if re_host: domain = "http://"+re_host.groups()[0]
    else: domain = ""
    return domain

###
def main():
    if len(sys.argv) != 2:
        print('usage: ./homework8.py file')
        sys.exit(1)

    filename = sys.argv[1]
    readfile_regex_image(filename)
    sys.exit(1)

if __name__ == '__main__':
  main()


#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Python for Tester - OneMount Class
# Quang Le - quangdle@gmail.com - 09/2021

import sys
import re
import io

"""Baby Names exercise

Định nghĩa hàm extract_names() dưới đây và gọi từ hàm main().

Cấu trúc các tag html trong các file baby.html như sau:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Các bước nên làm tuần tự:
 -Trích xuất năm
 -Lấy và in ra tên và thứ hạng phổ biến
 -Xây danh sách [year, 'name rank', ... ] và in ra
 -Sửa hàm main() để dùng hàm extract_names.
"""

def extract_names(filename):
  """
  Cho một file .html, trả ra list bắt đầu bằng năm, 
  theo sau bởi các chuỗi tên-xếp hạng theo thứ tự abc.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  year = 0
  list_data = []
  with open(filename, "r", encoding='utf-8-sig') as file:
    for line in file:
      if(year == 0):
        re_year = re.search("Popularity in (\d+)", line)
        if(re_year): 
          year = re_year.groups()[0]
          
      re_name = re.findall("<td>(\d+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>", line)  
      if(re_name):
        list_data.append(re_name[0][1] + " " + re_name[0][0])
        list_data.append(re_name[0][2] + " " + re_name[0][0])
  list_data.sort(); 
  list_data.insert(0, year)     
  return list_data  


    


def main():
  # Chương trình này có thể nhận đối số đầu vào là một hoặc nhiều tên file
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # Với mỗi tên file, gọi hàm extract_names ở trên và in kết quả ra stdout
  # hoặc viết kết quả ra file summary (nếu có input --summaryfile).
  list_data_name = []
  for filename in args:
    list_data_name += extract_names(filename)
  if(summary):
    with open('summary.txt', 'w') as file:
      file.write("\n".join(list_data_name))
      print("Vui lòng mở file summary.txt để xem kết quả")
  else:
      print(list_data_name)   
  
if __name__ == '__main__':
  main()

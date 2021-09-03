# Bài 1: Chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng
print("\n---- Bài 1: Print Star ----\n")
try:
    n = abs(int(input("Nhập số nguyên bạn muốn in ra ")))
    star_str = " *"
    space_str = "  "
    #in ra hình 1:
    print("\n ----- Hình star 1 -----")
    for num in range(n):
        space_number  = n - num + 1
        star_number= num + 1
        print(space_number * space_str + (star_number * star_str))
   
    #in ra hình 2
    end_str = "\n"
    print("\n ----- Hình star 2 -----")
    for num in range(n):
        space_number  = n - num + 1
        star_number= num + 1
        if star_number == n:
            end_str =""
        print(space_number * space_str + (star_number * star_str), end = end_str)
        

    for num in range(n):
        star_number = n - num 
        space_number  = n + 2
        if num == 0: space_number = 0
        print(space_number * space_str, (star_number * star_str).strip())


    #in ra hình 3
    end_str = "\n"
    print("\n ----- Hình star 3 -----")   
    for num in range(n):
        space_number  = n - num + 1
        star_number= num + 1
        if star_number <= 2 or star_number == n:
            star_text = star_number * star_str
        else:
            star_text = star_str +  space_str * (star_number - 2) + star_str
        if star_number == n:
            end_str =""
        print(star_text.rstrip() , end = end_str)
        

    for num in range(n):
        star_number = n - num 
        space_number  = n  + num
        if num == 0: space_number = 0
        if star_number <= 2 or star_number == n:
            star_text = star_number * star_str
        else:
            star_text = star_str +  space_str * (star_number - 2) + star_str
        print(space_number * space_str + star_text)

except:
    print("Bạn cần nhập số nguyên")

# Bài 2: Trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list
print("\n---- Bài 2: Đếm số ----\n")    
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
print(f"My List: {my_list}")
my_dict = {}
for value in my_list:
    total = my_dict.get(value)
    if(total):
        my_dict[value] = total + 1
    else:
        my_dict[value] = 1      

print(f"\nMy dict: {my_dict}\n")    


# Bài 3: Chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.
print("\n---- Bài 3: Đếm ngược đến XMas ----\n") 
import datetime
import time

is_stop = False
while is_stop == False:
    for i in range(5):
      time_xmas = datetime.datetime(2021,12,24)
      time_now = datetime.datetime.fromtimestamp(time.time())
      time_total = time_xmas - time_now
      print(f"Countdown to Xmas 2021: {time_total}")
      time.sleep(5)

    stop_str = input("Bạn có muốn dừng lại không? (Y/N): ")
    if stop_str.lower() == 'y':  
      is_stop = True


# Bài 4: Unique value Dictionary.
print("\n---- Bài 4: Unique value Dictionary ----\n")
def unique_value_dict(list_dict):
    dict_value = {}
    for dict in list_dict:
        all_values = list(dict.values())
        for value in all_values:
            dict_value[value] = 1

    list_unique = list(dict_value.keys())
    print(f"\n{list_dict} = {list_unique}")

print("Ví dụ về tìm unique: ")
#Ví dụ 1 của đề
dicts = [dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
unique_value_dict(dicts) 

#Ví dụ 2 của đề
dicts = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_value_dict(dicts) 

# ví dụ về trường hợp nhiều Dictionary trong 1 list
dicts =  [dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22), dict(Trang=56, Thu=56, Ngoc=57, Thanh=52, Yen=55, Hang=56, Thuy=22)]
unique_value_dict(dicts) 


# Bài 5: For/While loop và Dictionary/Tuple/Set - Find Pair
print("\n---- Bài 5: Find Pair ----\n")
def find_pair(list_a, sum):
    list_result = []
    for first_value in list_a:
        for second_value in list_a:
            if first_value + second_value == sum and first_value < second_value:
                list_result.append((first_value, second_value))

    print(f"List các cặp có tổng bằng {sum} là: {list_result}")   

list_example = [3, 6, 7, 9, 11, 12]
print(f"List ví dụ: {list_example}")
find_pair(list_example, 18) 
is_run_continue = True 
while is_run_continue:
  try:
    sum = int(input("Mời bạn nhập số bạn muốn kiểm tra (int): "))
    find_pair(list_example, sum)
    is_run_continue = False 
  except:
    print('Bạn cần nhập  số nguyên') 
    is_run_continue = True 
       



# Bài 1: Chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng
print("\n---- Bài 1: Print Star ----\n")
try:
    n = abs(int(input("Nhập số nguyên bạn muốn in ra ")))
    star_str = " *"
    space_str = "  "
    for star_number in range(n):
        space_number  = n -star_number 
        print((space_number + 1) * space_str + (star_number + 1) * star_str)

    for star_number in range(n):
        space_number  = n -star_number 
        print((star_number + 1) * star_str + (space_number + 1) * space_str )

except:
    print("Bạn cần nhập số nguyên")

# Bài 2: Trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list
print("\n---- Bài 1: Đếm số ----\n")    

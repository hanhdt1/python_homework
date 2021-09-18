**Hướng dẫn chung.**
* Code phần Easy trong file easy.py
* Code phần Medium trong file medium.py
* Code phần Hard trong file babynames.py (phía dưới những phần được ghi chú # +++your code here+++)
    Bạn được cung cấp 3 file inputs đầu vào babyxxxx.html

* Tùy thuộc vào setup của bạn, bạn có thể chạy lệnh 
    'python main.py' hoặc 'python3 main.py' để chạy unittest kiểm tra code của bạn có cho đáp án chính xác không cho các bài phần Easy và Medium. Ban đầu bạn sẽ gặp kết quả 'FAILED (failures=4)'. 
    Nếu code đúng hết thì chạy lệnh trên sẽ có kết quả là 
    -----------------------------------
    Ran 4 tests in 0.010s

    OK
    -----------------------------------

# Easy [1] Day different:
Viết hàm day_diff() nhận vào ngày phải release sản phẩm và ngày đội dev viết xong code. Tính số ngày mà team test có để test sản phẩm (= release_date - code_complete_day). Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05

# Easy [2] Alphabet and Number:
Viết hàm alpha_num() tìm tất cả những từ trong một câu có chứa cả chữ cái và số. Trả ra danh sách các từ như vậy trong một câu.
Vd:
str1 = "Emma25 is Data scientist50 and AI Expert"
alpha_num(str1) == ["Emma25", "scientist50"]

# Medium [1] Anagram Number:
Viết hàm anagram_number() có đầu vào là một số nguyên và trả ra True nếu sau khi đảo ngược thứ tự các chữ số của số đó vẫn cho ta số ban đầu. Trả ra False nếu không giống.
vd: anagram_number(121121) == True
    anagram_number(1254) == False

# Medium [2] Roman to Integer
Các chữ số La Mã được thể hiện bằng bảy biểu tượng khác nhau: I, V, X, L, C, D và M với
I=1; V=5; X=10; L=50; C=100; D=500; M=1000

Ví dụ: số 2 được viết là II bằng số La Mã, chỉ là hai chữ I được thêm vào với nhau. 12 được viết là XII, đơn giản là X + II. Con số 27 được viết là XXVII, là XX + V + II.

Chữ số La mã thường được viết từ lớn nhất đến nhỏ nhất từ trái sang phải. Tuy nhiên, số 4 không viết là IIII mà được viết là IV. Bởi vì I đứng trước V, chúng ta lấy 5 - 1 = 4. Nguyên tắc tương tự cũng áp dụng cho số chín, được viết là IX. Có sáu trường hợp phép trừ được sử dụng:

I có thể được đặt trước V (5) và X (10) để tạo thành 4 và 9.
X có thể được đặt trước L (50) và C (100) để tạo ra 40 và 90.
C có thể được đặt trước D (500) và M (1000) để tạo thành 400 và 900.
Cho một chữ số la mã dạng string, hãy viết hàm roman_to_int() chuyển nó thành một số nguyên.

# Hard [1] Baby Name
Xem yêu cầu trong file babynames.py
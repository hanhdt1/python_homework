# Hackathon 2 - Python

Nội dung: Project tổng hợp nội dung các phần OOP, Exception và Database cũng như các nội dung đã học trước đó

## Game đánh bài (3 cây)

Xây dựng game chơi bài 3 cây đơn giản, cho phép một số lượng người chơi nhất định tham gia. Trò chơi bao gồm 1 bộ bài (ở đây rút gọn còn 36 lá), mỗi lá bài có rank (A,2,3,4,5,6,7,8,9) và suit (spade, club, diamond và heart). Mỗi màn chơi, mỗi người chơi sẽ được chia 3 lá bài theo thứ tự, và dựa trên số điểm để tìm ra người chiến thắng.

## Yêu cầu:

-   Class Deck bao gồm 36 lá bài, Deck bao gồm class Card, tương ứng với mỗi lá bài
-   Class Player lưu thông tin của người chơi, cũng như các lá bài của người chơi
-   Class Game chứa các chức năng chính

Các chức năng:

-   Khởi tạo trò chơi, lưu thông tin của người chơi
-   Hiển thị menu hướng dẫn chơi/các chức năng
-   Thêm/bớt người chơi
-   Trộn bài và chia bài cho mỗi người chơi
-   Lật bài, hiển thị bộ bài của mỗi người chơi, tính điểm và thông báo người chiến thắng
-   Sau mỗi màn chơi, lưu lịch sử vào CSDL cho phép xem lại game gần nhất, hay thống kê thông tin như số game đã chơi, số game chiến thắng với mỗi người chơi

💡 Xem ảnh Gif đính kèm

Tạo CSDL với file sql đính kèm, hoặc sử dụng cấu hình sau:

```python
# Bao gồm bảng games và logs tương ứng với local
config = {
    'host': 'remotemysql.com',
    'user': 'UyMDXcxEoz',
    'password': 'lFJmWnNbEC',
    'database': 'UyMDXcxEoz'
}
```

-   Các file đính kèm sẽ cung cấp hướng dẫn và các chức năng cần thiết, có thể bổ sung hoặc thay đổi các phương thức
-   Xử lý exception (ví dụ trường hợp nhập dữ liệu không phù hợp)

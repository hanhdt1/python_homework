'''Kết nối CSDL'''
import mysql.connector as mysql
db = mysql.connect(
    host = "remotemysql.com",
    user = "UyMDXcxEoz",
    passwd = "lFJmWnNbEC",
    database = "UyMDXcxEoz"
)
cursor = db.cursor()
def log(winner, players):
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs

    Bảng games gồm tên người chiến thắng

    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''
    query = "INSERT INTO games (winner) VALUES ("+winner.name+")"
    cursor.execute(query)
    db.commit()
    game_id = cursor.lastrowid
    print(game_id)

    query = "INSERT INTO logs (game_id, player, cards, 	point, biggest_card) VALUES (%s, %s, %s, %s, %s)"
    ## storing values in a variable
    values = []
    for player in players:
        values.append((game_id, player.name, player.list_card(), player.point, player.biggest_card))

    cursor.executemany(query, values)
    db.commit()

    pass


def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    pass


def history():
    '''
    Lấy thông tin về lịch sử chơi

    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''

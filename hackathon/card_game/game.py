from os import name

from pymysql import NULL
from deck import Deck
from player import Player
import db


class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''
    players = [] 
    is_deal = False
    def __init__(self):
        pass

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        while(True):
            try:
                number_player = input("Nhập số người chơi: ")
                if not number_player.isdigit():
                    raise ValueError("Bạn chỉ được nhập số")
                number_player = int(number_player)
                if 2 <= number_player <= 12:    
                    for i in range(number_player):
                        name = input(f"Nhập tên người chơi {i+1}: ")
                        if name == "": name = f"Player{i+1}"
                        self.players.append(Player(name)) 
                    break;    
                else:
                    raise ValueError ("Bạn chỉ được nhập từ 2 đến 12 người chơi")        
            except BaseException as err:
                print(f"{err}")                          

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        if self.is_deal: text = "(Đã chia)"
        else: text =  "(Chưa chia)"
        print(" --------------------------------------")
        print(f'1. Danh sách người chơi ({len(self.players)})')
        print('2. Thêm người chơi')
        print('3. Loại người chơi')
        print(f'4. Chia bài {text}')
        print('5. Lật bài')
        print('6. Xem lại game vừa chơi')
        print('7. Xem lại lịch sử chơi')
        print('8. Công an đến, tốc biến')
        pass

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        print("Danh sách người chơi:")
        print("ID\tName")
        i = 0
        for player in self.players:
            i += 1
            print(f"{i}\t{player.name}")
        pass

    def add_player(self):
        '''Thêm một người chơi mới'''
        num = len(self.players)
        if(num == 12):
            raise ValueError("Đã đạt số người chơi tối đa, không thể thêm được nữa nhé")

        name = input(f"Nhập tên người chơi {num+1}: ") 
        if name == "": name = f"Player{num+1}"
        self.players.append(Player(name))
        pass

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        if len(self.players) ==2:
            raise ValueError("Tối thiểu phải có 2 người chơi, bạn không thể remove người chơi được")
        self.list_players()
        id = int(input("Nhập ID người chơi bạn muốn loại khỏi cuộc chơi: "))
        self.players.pop(id-1)
        pass

    def deal_card(self):
        '''Chia bài cho người chơi'''
        if self.is_deal:
            raise ValueError("Bài đã chia rồi, lật bài đi thôi")
        deck = Deck()
        deck.build()
        deck.shuffle_card()        
        for i in range (3):
            for player in self.players:
                player.add_card(deck.deal_card())
        self.is_deal = True  
        print("Bài đã chia xong, xuống tiền nào")      

    
    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        if not self.is_deal:
            raise ValueError("Chưa chia bài bạn ơi, chia đã rồi mới lật được nhé")
        for player in self.players:
            print (f"Người chơi {player.name}", end=": ")
            print(player.flip_card(), end="")
            print (f", Tổng điểm {player.point}, lá bài lớn nhất {player.biggest_card}")
        
        win = max(self.players)
        print(f"Chúc mừng {win.name} đã có tiền") 
        db.log(win, self.players)

        self.is_deal = False
        for player in self.players:
            player.remove_card()

    def last_game(self):
        game, logs = db.get_last_game()
        if game is not None:
            print ("Thời gian: ", game['play_at'], ' Người chiến thắng: ', game['winner'])
            for log in logs:
                print (f"Người chơi {log['player']}: {log['cards']}", end="")                
                print (f", Tổng điểm {log['point']}, lá bài lớn nhất {log['biggest_card']}")       

    def history(self):
        historys = db.history()
        list_str = ""
        count_all = 0
        if historys is not None:
            for history in historys:
               count_all += history['count']
               list_str += f"{history['winner']} thắng {history['count']} ván\n"   
        print (f"Hôm nay đã chơi: {count_all} ván")     
        print (list_str)  

                

           
        
    
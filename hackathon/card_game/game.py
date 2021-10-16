from os import name
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
        number_player = int(input("Nhập số người chơi: "))
        for i in range(number_player):
            name = input(f"Nhập tên người chơi {i+1}: ")
            self.players.append(Player(name))

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
            print("Đã vượt quá số người tối đa")
            return

        name = input(f"Nhập tên người chơi {num+1}: ") 
        self.players.append(Player(name))
        pass

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        self.list_players()
        id = int(input("Nhập ID người chơi bạn muốn loại khỏi cuộc chơi: "))
        self.players.pop(id-1)
        pass

    def deal_card(self):
        '''Chia bài cho người chơi'''
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
        max_point = 0
        win = self.players[0]
        for player in self.players:
            player.flip_card()
            if win.point < player.point:
                win = player
            elif win.point == player.point:
                if win.biggest_card < player.biggest_card:
                    win =  player

        print(f"Chúc mừng {win.name} đã có tiền")     
        self.is_deal = False
        for player in self.players:
            player.remove_card()
        #db.log(win, self.players)        

           
        
    
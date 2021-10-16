from logging import error, raiseExceptions
from game import Game
import db
def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    
    game = Game()
    game.setup()
    game.guide()
    i = 0
    while(i!=8):
        try:
            i = input("Nhập số bạn muốn chọn: ")
            if not i.isdigit():
                raise ValueError("Bạn chỉ được nhập số")
            i = int(i)    
            if i == 1:
                game.list_players()                
            elif i == 2:
                game.add_player()
            elif i == 3:
                game.remove_player()
            elif i == 4:
                game.deal_card() 
            elif i == 5: 
                game.flip_card()
            elif i == 6:
                game.last_game()
            elif i == 7:
                game.history()
            elif i != 8:
                raise ValueError("Bạn cần chọn các số từ 1 đến 8")
            game.guide()    
        except BaseException as err:
            print(f"{err}")        
    else:
        print("Đã kết thúc game")
            


if __name__ == '__main__':
    main()
    
   

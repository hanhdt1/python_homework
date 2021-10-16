from game import Game


def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    game = Game()
    game.setup()
    game.guide()
    i = 0
    while(i!=8):
        i = int(input("Nhập số bạn muốn chọn: "))
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

        game.guide()    
                
    else:
        print("Đã kết thúc game") 


if __name__ == '__main__':
    main()
   

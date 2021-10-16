class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''
    cards = []
    def __init__(self, name):  # dễ
        self.cards = []
        self.name = name

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        total_point = 0
        for card in self.cards:
            total_point += card.rank
        p = total_point % 10
        if p == 0: p = 10    
        return p  
    

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        return max(self.cards)

    def add_card(self, card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        self.cards.append(card)
        pass

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.cards = []

    

    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
        return ' '.join([str(c) for c in self.cards])
        
    def __gt__(self, other):
        if(self.point > other.point):
            return True
        elif self.point == other.point and self.biggest_card > other.biggest_card:
            return True
        else: return False    
                


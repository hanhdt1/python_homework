class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''
    ranks = ('', 'A', 2, 3, 4, 5, 6, 7, 8, 9)
    suits = ('♠', '♣', '♦', '♥')
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        '''Hiển thị lá bài'''
        return (str(self.ranks[self.rank]) + str(self.suits[self.suit]))
        pass

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
        
        if self.suit > other.suit:
            return True
        if self.suit == other.suit:
            if self.rank > other.rank:
                return True
            else:
                return False
        
    


     
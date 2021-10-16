
from random import shuffle
from card import Card
class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    cards  = []
    def build(self):
        '''Tạo bộ bài'''
        self.cards = []
        for i in range(1, 10):
            for j in range(4):
                self.cards.append(Card(i,j))
        pass

    def shuffle_card(self):
        '''Trộn bài'''
        shuffle(self.cards)
        pass

    def deal_card(self):
        '''Rút một lá bài từ bộ bài'''
        if len(self.cards) == 0:
            return
        return self.cards.pop()

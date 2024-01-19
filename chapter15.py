import random


class Deck():
    
    def __init__(self):
        self.all_cards = []
        self.deck1 = []
        self.deck2 = []

        for i in range(4):
            j = 1
            while j < 14:
                self.all_cards.append(j)
                j += 1
                if j == 13:
                    i += 1
        
        random.shuffle(self.all_cards)
        for i in range(26):
            self.deck1.append(self.all_cards[i])
            del self.all_cards[i]
        
        self.deck2 = self.all_cards

class Player():

    def __init__(self,name,deck):
        self.name = name
        self.deck = deck


class Game():

    def __init__(self,player1,player2):
        self.game = 0
        self.deck1 = player1.deck
        self.deck2 = player2.deck
        self.point1 = 0
        self.point2 = 0
        self.card1 = 0
        self.card2 = 0
        self.point = 0
        self.drow = 1
    
    def play(self):
        for i in range(26):
            self.point = 2 * self.drow
            self.card1 = self.deck1[i]
            self.card2 = self.deck2[i]

            if self.card1 > self.card2 :
                 self.point1 += self.point
                 self.drow = 1
            
            elif self.card2 > self.card1 :
                 self.point2 += self.point
                 self.drow = 1
            
            else :
                self.drow += 1
        
        return self.point1,self.point2






deck = Deck()
yuto = Player("yuto",deck.deck1)
kamijo = Player("kamijo",deck.deck2)
game = Game(yuto,kamijo)
print(kamijo.deck)
print(game.play())






        

    



    


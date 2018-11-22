class Card(object):
    def __init__(self,number,colour):
        self.number=number
        self.colour=colour
class Deck(Card):
    def __str__(self):
        self=[]
        for i in range(52):
            self[i]={ self.number
                     self.colour
                }
class Hand(Card):
    def __str__(self):
        self=[]
        for i in range(5):
            self[i]={ self.number
                     self.colour
                }
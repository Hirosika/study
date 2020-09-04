from random import shuffle

class Card:
    suits = ["hearts", "clubs", "diamonds", "spades"]
    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]
    
    def __init__(self):
        self.cards = [(v, s) for v in self.values[2:] for s in self.suits]
        shuffle(self.cards)
        
class Player:
    def __init__(self, n, p=0):
        self.name = n
        self.points = p

    def draw(self, d):
        self.value = d.cards.pop() 
    
class Game:
    def __init__(self):
        self.deck = Card()
        self.p1 = Player("Player1")
        self.p2 = Player("Player2")
        self.round = 1
        
    def compare(self):
        self.p1.draw(self.deck); self.p2.draw(self.deck)
        print(f"Player1 drew {self.p1.value[0]} of {self.p1.value[1]}",
              f"Player2 drew {self.p2.value[0]} of {self.p2.value[1]}",
              sep = "\n")
        if self.p1.value < self.p2.value:
            bigger =  self.p2
        else:
            bigger =  self.p1
        print(f"{bigger.name} takes the round!"); bigger.points += 1
        
    def play(self):
        while self.deck.cards:
            print(f"Round {self.round}/26!"); self.round += 1
            self.compare()
        if self.p1.points < self.p2.points:
            winner = self.p2
        elif self.p1.points > self.p2.points:
            winner = self.p1
        else:
            print("Draw!")
            return None
        print(f"{winner.name} won the game "
              f"by {abs(self.p1.points - self.p2.points)} points!")
            
game = Game()
game.play()


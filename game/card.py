import random

#Class: Card(self)
#Method: Generate deck (self) *Teigen*
#-Initializes the class and starts a new instance
#-Return DECK (array)

#Method: Generate Card(self) *Teigen*
#-Will generate a card with a random number between 1 and 13
#-Return CARD (int)

class card:
    #responsibility: to initialize the creation of the card
    #and create the card with a value between 1-13

    #attributes: value(int) the point value of the card
    
    def _init_(self):
        #a new instance of a card

        #args: self (card): an instance of Card class

        self.value = 0
        

    def generate(self):
        #generates a new card with a random point value between 1-13

        #args: self(card): an instance of Card class

        self.value = random.randint(1, 13)
        return self.value
        
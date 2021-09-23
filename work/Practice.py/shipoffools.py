import random

class die:
    def __init__(self):
        self._value = random.randint(1,6)

    def get_value(self):
        return self._value

    def roll(self):
        self._value = random.randint(1,6)
        

class DiceCup:
    
    def __init__(self):
        self.bank_list = []
        self._dice = []  
        for _ in range(5):
            self._dice.append(die())
            
    def value(self, index):      
        return self._dice[index].get_value()
    
    def bank(self, index): 
        #if index not in self.bank_list:  
        self.bank_list.append(index)
    
                
    def is_banked(self, index):
        return index in self.bank_list

    def release(self, index):
        self.bank_list.remove(index)
        
    def release_all(self):
        for i in self.bank_list:
            self.bank_list.remove(i)
        
    def roll(self):
        for die in self._dice:
            if die not in self.bank_list:
                return die.roll()
    
    def find_value(self, value): #funktion som finner värdet på tärningen
        found = False
        for i, die in enumerate(self._dice):
            if not self.is_banked(i) and die.get_value() == value:
                found = True
        return found
    
    def find_index(self, value): #funktion som finner index värdet på tärningen
        _index = 0
        for k, die in enumerate(self._dice):
            if not self.is_banked(k) and die.get_value() == value:
                _index = k 
        return _index
        

class ShipOfFoolsGame:
    def __init__(self, winning_score = 50):
        self._cup = DiceCup()
        self.winning_score = winning_score

    def turn(self):
        self.crew_list = []
        has_ship = False
        has_captain = False
        has_mate = False
        

        # This will be the sum of the remaining dice, i.e., the score.
        self.crew = 0
        # Repeat three times
        for _ in range(3):
            self._cup.roll()

            if not has_ship and self._cup.find_value(6):
                self._cup.bank(self._cup.find_index(6))
                has_ship = True

            if has_ship and not has_captain and self._cup.find_value(5):
                self._cup.bank(self._cup.find_index(5))
                has_captain = True
            
            if has_captain and not has_mate and self._cup.find_value(4):
                self._cup.bank(self._cup.find_index(4))
                has_mate = True
            
        #Counts last two dices
            if has_ship and has_captain and has_mate:
                for index in range(5):
                    if not self._cup.is_banked(index) and self._cup.value(index) > 3:
                        self._cup.bank(index)

        #Adds the last dices if value is below 3.
            if has_ship and has_captain and has_mate:
                for index in range(5):
                    if not self._cup.is_banked(index):
                        self._cup.bank(index)
        
        if has_ship and has_captain and has_mate:
            for x in self._cup.bank_list:
                self.crew_list.append(self._cup.value(x))
            self.crew = sum(self.crew_list) - 15
        
        else:
            self.crew = 0    

        return self.crew
        

class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0        

    def current_score(self): 
        return self._score        

    def reset_score(self):
        self._score = 0
    
    def play_turn(self, game):
        game = ShipOfFoolsGame()
        self._score += game.turn()
        

class PlayRoom:
    def __init__(self):
        self._players = []
        self._winner = ''
        
    def set_game(self, game):
        self._game = game
        
    def add_player(self, player):
        self._players.append(player)
        
    def reset_scores(self):
        for i in self._players:
            Player.reset_score(i)
    
    def play_round(self):
        for player in self._players:
            player.play_turn(self._game)           
    
    def game_finished(self):
        finished = False
        for i in self._players:
            if Player.current_score(i) >= self._game.winning_score:
                finished = True
        return finished

    
    def print_scores(self):
        for i in self._players:
            print('Player',i._name,'has:',Player.current_score(i))
        
    def print_winner(self):
        for x in self._players:
            if Player.current_score(x) >= self._game.winning_score:
                self._winner = x._name
                print('The winner is:',self._winner,'With the score:',Player.current_score(x))


if __name__ == "__main__":

    def main():
        loop = True
        while loop:
            try:
                player_amount = int(input('Amount of players:'))
                player_name = [str(input('Name:')) for _ in range(player_amount)]
                room = PlayRoom()
                room.set_game(ShipOfFoolsGame())
                for ele in player_name:
                    room.add_player(Player(ele))
                room.reset_scores()
                while not room.game_finished():
                    room.play_round()
                    print('----')
                    room.print_scores()
                print('----')
                room.print_winner()
                print('1. Play again \n2 Quit program')
                try:
                    player_choice = int(input('Your choice:'))
                    if player_choice == 1:
                        print('Lets play again!')
                    elif player_choice == 2:
                        loop = False
                except ValueError:
                    print('Wrong input')

            except ValueError: 
                print('Wrong input')
    
    main()
    

    

   

    



    
    
   
    
                
            
   
    
   
    
        





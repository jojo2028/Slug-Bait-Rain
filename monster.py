import sys

from Character_Class import Character
from monster import Dragon
from monster import Goblin
from monster import Troll

class Game(object):
    def setup(self):
        self.player = Character()
        self.monsters = [Goblin(), Troll(), Dragon()]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monster.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        # Check to see if the monster attacks
        if self.monster.attack():
        #if so, tell the player
            print ('{} is attacking!').format(self.monster)
            #check if the player wants to dodge
            if raw_input('Dodge? Y/N ').lower() == 'y':
                #if so, see if the dodge is successful
                if self.player.dodge():
                    #if it is, move on
                    print ('You dodged the attack!')
                #if it's not, remove one player hit point
                else:
                    print ('You got hit anyway!')
                    self.player.hit_points -= 1
            else:
                print ('{} hit you for 1 point!').format(self.monster)
                self.player.hit_points -= 1
        #if the monster isn't attacking, tell that to the player too
        else:
            print ('{} is not attacking this turn.').format(self.monster)

    def player_turn(self):
        #Let the player attack, rest, or quit
        player_choice = raw_input('[A]ttack', '[R]est', '[Q]uit').lower()
        #if they attack:
        if player_choice == 'a':
            print ('Yor are attacking {}!').format(self.monster)
            #See if the attack is successful
            if self.player.attack():
                #if so, see if the monster dodges
                if self.monster.dodge():
                    #if  dodged, print that
                    print ('{} dodged your attack!').format(self.monster)
                #If not dodged, substruckt the right num of hit points from the monster
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1

                    print ('You hit {} with your {}!').format(self.monster, self.player.weapon)
            else:
                print ('You missed!')
        #if they rest:
        elif player_choice == 'r':
            #call the player.rest() method
            self.player.rest()
        #if they quit, exit the game    
        elif player_choice == 'q':
            sys.exit()
        #if they pick anything else, re-run this method
        else:
            self.player_turn()

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print ('You killed {}!').format(self.monster)
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print ('\n' + '=') * 20
            print ('self.player')
            self.monster_turn()
            print ('-') * 20
            self.player_turn()
            self.cleanup()
            print ('\n' + '=') * 20

        if self.player.hit_points:
            print ('You Win!')
        elif self.monsters or self.monster:
            print ('You lose!')
        sys.exit()

Game()


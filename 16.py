# Imagine you are creating a Super Mario game.
# You need to define a class to represent Mario.
# What would it look like?
# If you aren't familiar
# with SuperMario, use your own favorite video or board game to model
# a player.

class SuperMario:
    Character = 'Mario'

    def __init__(self,life,height, speed, level):
        self.life = life
        self.height = height
        self.speed = speed
        self.level = level

    def marioInfo(self):
        print(self.Character)
        print('life:',self.life)
        print('height:',self.height)
        print('speed:', self.speed)
        print('level:',self.level)

    def move(self,key):
        #Move acc to mouse directions
        #Can Jump too
        print('moving')

make = SuperMario(3,2,4,5)
make.marioInfo()
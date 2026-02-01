class Hero:
    #Class construction
    def __init__(self, nick, hp, lvl):
        #Class attributes
        self.nick = nick
        self.hero_hp = hp
        self.hero_lvl = lvl
    def action(self):
        return f"{self.nick} base action activate!"


#Object/example of the class
kirito = Hero("Kirito", 1000, 100)  # This creates a Hero object
asuna = Hero("Asuna", 1100, 101) 
my_int = 123
my_str = "text"
print(type(my_int))
print(type(kirito))

#print(kirito.hero_lvl)
#print(asuna.hero_lvl)

#print(kirito.action())
#print(asuna.action())




class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        Player.count += 1

    @staticmethod
    def get_count():
        return Player.count

messi = Player('Messi')
ronaldo = Player('Ronaldo')

print(messi.get_count())
print(ronaldo.get_count())
print(Player.get_count())

# print(Player.count)
#
# print(messi.count)
# print(ronaldo.count)
#
# Player.count = 100
#
# print(Player.count)
#
# print(messi.count)
# print(ronaldo.count)

# messi.count = 100
#
# print(Player.count)//2
#
# print(messi.count)//100
# print(ronaldo.count)//2

from abc import ABC,abstractmethod


# class GamingConsole(ABC):
#     @abstractmethod
#     def up(self): pass
#
#     @abstractmethod
#     def down(self): pass
#
#     @abstractmethod
#     def left(self): pass
#
#     @abstractmethod
#     def right(self): pass


class MarioGame:
    def up(self): print('jump')

    def down(self): print('goes into a hole')

    def left(self): pass

    def right(self): print('Go Forward')


class ChessGame:
    def up(self): print('Move piece up')

    def down(self): print('Move piece down')

    def left(self): print('Move piece left')

    def right(self): print('Move piece right')


# games = [ChessGame(), MarioGame()]
#
# for game in games:
#     game.up()
#     game.down()
#     game.left()
#     game.right()

class Test1:
    def method(self): print("Test1")

class Test2:
    def method(self): print("Test2")

tests = [Test1(),Test2()]

for test in tests:
    test.method()


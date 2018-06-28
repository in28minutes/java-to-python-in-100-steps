from abc import ABC, abstractmethod

class AbstractRecipe(ABC):

    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.cleanup()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def do_the_dish(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class Recipe1(AbstractRecipe):

    def get_ready(self):
        print('Get raw materials')
        print('Get utensils')

    def do_the_dish(self):
        print('do the dish')

    def cleanup(self):
        print('clean utensils')


# TypeError: Can't instantiate abstract class AbstractRecipe
# with abstract methods cleanup, do_the_dish, get_ready
# recipe = AbstractRecipe()

recipe = Recipe1()

recipe.execute()
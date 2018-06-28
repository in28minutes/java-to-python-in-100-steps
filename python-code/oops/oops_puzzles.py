class Country:
    # def __init__(self):
      #  print('constuctor 1')

    def __init__(self, name="Default"):
        self.name = name
        print('constuctor 2')

    def instance_method(self):
        print('instance method')


default_country = Country()
india = Country('India')

print(default_country.name)
print(india.name)
#TypeError: __init__() missing 1 required positional argument: 'name'

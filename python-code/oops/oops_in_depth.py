class Planet:
    def __init__(self, name, distance_from_sun):
        self.name = name
        self.distance_from_sun = distance_from_sun

earth = Planet('Earth', 200)
mars = Planet('Mars', 500)

earth.speed = 10000
print(earth.speed)

# mars.name = 'Mars'
print(mars.name)
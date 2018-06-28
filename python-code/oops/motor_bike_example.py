class MotorBike:

    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def __repr__(self):
        return repr((self.gear, self.speed))


# instance 1 or object 1
honda = MotorBike(3, 50)

# instance 2 or object 2
ducati = MotorBike(1, 10)

print(honda)
print(ducati)
from car import Car

if __name__ == '__main__':
    toyota = Car('sedan', 'corolla', "blue", 150)
    print(toyota.type, toyota.model)
    toyota.color = "red"
    print(toyota.color)
    toyota.speed = 200
    print(toyota.speed)
    honda = toyota
    honda.model = "civic"
    print(toyota.model, honda.model)
    audi = Car("Suv", "Q7", "black", 220)
    audi.color = "white"
    honda = audi
    print(honda.type, audi.type)

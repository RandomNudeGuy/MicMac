from car import Car

if __name__ == '__main__':
    first_car = Car('Suzuki', 'Smift', 100, 'Gasolin', 'Red')
    second_car = Car('Honda', 'Civic', 200, 'Diesel', 'Black')

    print(first_car.brand)
    print(first_car.subbrand)
    print(first_car.speed)
    print(first_car.fuel)
    print(first_car.color)
    print()
    print(second_car.brand)
    print(second_car.subbrand)
    print(second_car.speed)
    print(second_car.fuel)
    print(second_car.color)

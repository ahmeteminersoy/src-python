class Car:
    def __init__(self, platenumber, size):
        self.platenumber = platenumber
        self.size = size
class CarPark:
    def __init__(self, size, hourlyprice) :
        self.size = size
        self.hourlyprice = hourlyprice
        self.carlist = []
    def calculateparking(self, entrydate, exitdate, car):
        return (exitdate - entrydate) * self.hourlyprice * car.size
        
    def parkCar(self, car, entrydate):
        if isinstance(car, Car):
            if self.size < car.size:
                print("You cannot park the car, the carpark is full..!")
            self.size -= car.size
            self.carlist.append(car)


if __name__ == "__main__":
    carpark = CarPark(10, 10)
    a = Car("34EDB511", 10)
    ticket = carpark.calculateparking(3, 5, a)
    print(ticket)
            





    
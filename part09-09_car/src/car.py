# WRITE YOUR SOLUTION HERE:
#step1 : create a class name is Car , it has two attrebute __amount_of_petrol and __odometer
#step2 : create a function name is fill_up() wich fill_up the __amount_of_petrol to the max (60l)
#step3 : create a function name is drive() wich drive the car the distance give it if distance <= __amount_of_petrol else __amount_of_petrol - distance and __odometer += __amount_of_petrol
#step4 : create a method __str__ wich print __amount_of_petrol and __odometer

#step1 : create a class name is Car , it has two attrebute __amount_of_petrol and __odometer
class Car:
    def __init__(self):
        self.__amount_of_petrol = 0
        self.__odometer = 0

    #step2 : create a function name is fill_up() wich fill_up the __amount_of_petrol to the max (60l)
    def fill_up(self):
        self.__amount_of_petrol = 60

    #step3 : create a function name is drive() wich drive the car the distance give it if distance <= __amount_of_petrol else __amount_of_petrol - distance and __odometer += __amount_of_petrol
    def drive(self,km:int):
        if km <= self.__amount_of_petrol:
            self.__amount_of_petrol -= km
            self.__odometer += km
        else:
            self.__odometer += self.__amount_of_petrol
            self.__amount_of_petrol = 0

    #step4 : create a method __str__ wich print __amount_of_petrol and __odometer
    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__amount_of_petrol} litres"
        
if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)

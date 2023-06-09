"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""
from prac_06.car import Car

def main():
    my_car = Car("My car", 180)
    my_car.drive(30)
    print(f"fuel: {my_car.fuel}")
    print(my_car)
    limo = Car(100)

    limo.add_fuel(20)

    print(f"Fuel amount in the car: {limo.fuel} litres")

    distance_driven = limo.drive(115)

    print(f"Distance driven: {distance_driven} km")


    print(limo)


main()

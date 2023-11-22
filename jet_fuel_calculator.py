# Author: Jeremiah E. Ochepo
# Date Written: 04/11/2020
# Date Updated: 04/11/2020
# Code Description: Simple Calculator for Jet Fuel Metrics

def liters_amount(liters_per_gallon, gallons):
    liters = round(liters_per_gallon * gallons, 2)
    return f"{gallons} gallons of jet fuel is equivalent to {liters} liters."


def barrel_amount(barrels_per_gallon, gallons):
    barrels = round(barrels_per_gallon * gallons, 2)
    return f"{gallons} gallons of jet fuel requires {barrels} barrels of oil."


def pounds_co2(pounds_per_gallon, gallons):
    pounds = round(pounds_per_gallon * gallons, 2)
    return f"{gallons} gallons of jet fuel produce {pounds} pounds of CO2."


def british_unit(buts_per_gallon, gallons):
    buts = round(buts_per_gallon * gallons, 2)
    return f"{gallons} gallons of jet fuel produce {buts} BTUs of energy."


def jet_weight(weight_per_gallon, gallons):
    weight = round(weight_per_gallon * gallons, 2)
    return f"{gallons} gallons of jet fuel weighs {weight} pounds."


def gallon_in_dollars(cost_per_gallon, gallons):
    cost = round(cost_per_gallon * gallons, 2)
    return f"{gallons} gallons of jet fuel cost ${cost}."


def travel_time(speed, gallons):
    flight_time = (gallons / speed) * 60  # time = distance / speed
    fly_hour = int(flight_time // 60)
    fly_mins = int(flight_time % 60)
    return f"Flight time of a 787 aircraft: {fly_hour} hours {fly_mins} minutes."


def main():
    active_flag = True
    while active_flag:
        try:
            # Set the number of gallons
            gallons = float(input("Please enter the number of gallons: "))

            # Print Output
            print(f"Number of gallons is: {gallons}")
            print(liters_amount(3.7554, gallons))
            print(barrel_amount(4, gallons))
            print(pounds_co2(21.092, gallons))
            print(british_unit(128100, gallons))
            print(jet_weight(6.7, gallons))
            print(gallon_in_dollars(1.88, gallons))
            print(travel_time(1600, gallons))

            # End while Loop
            active_flag = False
        except ValueError:
            # Display error message then ask the user for input again
            print("Entry has to be a number. Please try again.\n")


if __name__ == "__main__":
    main()

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = create_taxis()
    current_taxi = None
    total_bill = 0.0

    print("\nLet's drive!")
    choice = None
    while not choice == "q":
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'c':
            # Choose a taxi
            current_taxi = choose_taxi(taxis)
            if current_taxi:
                print(f"You have chosen: {current_taxi}")

        elif choice == 'd':
            # Drive the chosen taxi
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                trip_cost = drive_taxi(current_taxi)
                total_bill += trip_cost

        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def create_taxis():
    """Create and return a list of taxi objects"""
    return [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]


def display_taxis(taxis):
    """Display the available taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Allow user to choose a taxi and return the selected taxi"""
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input; please enter a number.")
        return None


def drive_taxi(current_taxi):
    """Drive the selected taxi and calculate the fare"""
    distance = float(input("Drive how far? "))
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    return trip_cost


if __name__ == "__main__":
    main()

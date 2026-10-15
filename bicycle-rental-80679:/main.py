from bicycle import Bicycle


def main():
  
    bike1 = Bicycle("B001", "Mountain Bike", 10.0)
    bike2 = Bicycle("B002", "City Bike", 7.0)
    bike3 = Bicycle("B003", "Road Bike", 12.0)
    bike4 = Bicycle("B004", "Electric Bike", 15.0)

    bicycles = [bike1, bike2, bike3, bike4]
    
    print("=== Bicycle Rental System ===")
    print("\n Available bicycles:")

    for bike in bicycles:
        print(bike)

    print("\nSuccessful Rental")

    try:
        bike1.rent()
        print(f"{bike1.item_id} rented successfully.")
    except RuntimeError as error:
        print(f"Rental error: {error}")

    print("\n Unsuccessful Rental")

    try:
        bike1.rent()
        print("Rental successful.")
    except RuntimeError as error:
        print(f"Rental error: {error}")

    print("\n Rental Cost ")

    try:
        hours = 3
        cost = bike1.calculate_rental_cost(hours)
        print(f"Rental cost for {hours} hours: €{cost:.2f}")
    except ValueError as error:
        print(f"Cost error: {error}")

    print("\n Change Rental Price ")

    try:
        bike2.set_rental_price(8.0)
        print(f"New hourly price for {bike2.item_id}: "
              f"€{bike2.rental_price:.2f}")
    except ValueError as error:
        print(f"Price error: {error}")

    print("\n Return Bicycle ")

    try:
        bike1.return_item()
        print(f"{bike1.item_id} returned successfully.")
        print(bike1)
    except RuntimeError as error:
        print(f"Return error: {error}")

    print("\n Input Validation ")

    try:
        bike3.set_rental_price(-5)
    except ValueError as error:
        print(f"Invalid price rejected: {error}")

    print("\n Alternative Constructor")

    standard_bike = Bicycle.create_standard_bicycle(
        "B005", "Standard Bike"
    )

    print(standard_bike)


if __name__ == "__main__":
    main()

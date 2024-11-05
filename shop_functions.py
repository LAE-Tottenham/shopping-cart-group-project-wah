import pyfiglet
from geopy.distance import geodesic

def shopping_cart():
    # Display title
    title = pyfiglet.figlet_format("Online Shopping Cart")
    print(title)

    # List of products with their prices
    products = {
        'Bread': 1.20,
        'Milk': 1.15,
        'Chocoloate': 0.5,
        'Flour': 1.25,
        'Water': 1.00,
        'Sweets': 2.00,
        'Coke': 1.70,
        'Monster': 1.80,
        'Lemonade': 0.90,
        'Vodka': 14.20,
    }

    # Display products
    print("Available Products:")
    for product, price in products.items():
        print(f"{product}: £{price:.2f}")

    # User selects products
    selected_products = []
    while True:
        choice = input("Select a product (or type 'done' to finish): ")
        if choice.lower() == 'done':
            break
        if choice in products:
            selected_products.append(products[choice])
        else:
            print("Invalid choice. Please try again.")

    # Calculate total price
    total_price = sum(selected_products)
    print(f"Total Price: £{total_price:.2f}")

    # Get delivery postcode and calculate delivery price
    delivery_postcode = input("Enter your delivery postcode: ")

    delivery_location = (51.6115, -0.0697)
    user_location = get_coordinates(delivery_postcode)

    # Calculate delivery cost
    if user_location:
        distance = geodesic(delivery_location, user_location).miles
        delivery_cost = distance
        total_cost = total_price + delivery_cost
        print(f"Delivery Cost: £{delivery_cost:.2f}")
        print(f"Total Cost (including delivery): £{total_cost:.2f}")
    else:
        print("Could not calculate delivery distance. Please check your postcode.")


def get_coordinates(postcode):
    return (51.5074, -0.1278)

if __name__ == "__main__":
    shopping_cart()

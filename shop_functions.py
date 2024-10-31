menu = {
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

def start_shop():
  while True:
      print("What you would like to buy? ")
      print('\n'.join("{}: {}".format(k, v) for k, v in menu.items()))
      item = input("Enter the item you want to buy (or 'q' to quit): ").strip()
      if item.lower() == 'q':
        break
      if item in menu:
        try:
          quantity = int(input(f"How many {item} do you want? "))
          if quantity <= 0:
            print("Please enter a valid quantity (greater than 0).")
            continue
          
          total_cost = menu[item] * quantity
          print(f"Total cost for {quantity} {item}: £{total_cost:.2f}")
        except ValueError:
          print("Invalid quantity. Please enter a number.")
      else:
        print(f"Sorry, '{item}' is not available.")

start_shop()

import geopy.distance
def calculate_delivery_cost(postcode):
  london_coords = (51.5814, 0.0841)  # Coordinates for London N17 0BX
  try:
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.geocode(postcode)
    if location is None:
      raise ValueError("Invalid postcode.")
    
    target_coords = (location.latitude, location.longitude)

    distance_miles = geopy.distance.geodesic(london_coords, target_coords).miles
    delivery_cost = distance_miles * 1.00
    return delivery_cost
  except ValueError as e:
    print(f"Error: {e}")
    return None

postcode = input("Enter a postcode:  ")
cost = calculate_delivery_cost(postcode)
if cost is not None:
  print(f"Delivery cost for {postcode}: £{cost:.2f}")

"""
an app to suggest band name based on city user grew up in and user pet name
"""
print("welcome to the band name generator.")
city = input("What's the name of the city you grew up in? ")
pet = input("What's the name of your pet? ")
print("generating name ...")
print(city.capitalize() + " " + pet.capitalize())


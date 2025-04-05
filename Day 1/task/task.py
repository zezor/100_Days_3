
def band_name_creation():
    print("Welcome to Band Name Generator")
    name = input("What is your name?")

    pet_name = input("What is the name of your pet?")
    city_name = input("What is the name of the city you grew in?")

    band_name = pet_name + "_" + city_name
    print(name + ", Your band name is " +band_name)
band_name_creation()


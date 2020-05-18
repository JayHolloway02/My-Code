#Diner Menu

def intro():
    print("Hi, Welcome to Jupiter Diner.")
    print("We offer all day breakfeast, lunch, and dinner. ")
    menusss()

def menusss():
    menuoption = input("Would you like to order Breakfeast, Lunch, Or Dinner? ")
    if menuoption == "Breakfeast" or menuoption == "breakfeast":
        print("""
                    Here is our breakfeast menu

                Pancakes: Regular, Blueberry, Chocolate
                Waffles: Regular or Chocolate
                Donuts: Glaze, Chocolate, Sprinkle, Jelly Filled
                Bacon: Bacon or Canadian Bacon
                Sasuage: Regular or Smoked
                Eggs: Scrambled, Omelet, Sunny Side Up, Fried
                Coffee: Black, Milk & Creamer, Latte, Americano, Mocha
                Tea: Black, Green, Olong, Lemon
                Juice: Orange Juice, Lemonaid, Grape Juice
                Milkshakes: Strawberry, Blueberry, Blackberry, Raspberry 
                                                        """)

        breakfeast = input("What would you like to order? ")
        print("Your order is:" ,breakfeast)



    elif menuoption == "Lunch" or menuoption == "lunch":
        print("""
                    Here is our Lunch menu

                Sandwich: Cheese, Turkey, Chicken, Steak, Salami, BLT
                Burgers: Regular, Bacon, Veggie, Chicken, Steak
                Fries: Steak, Resturant, Curly
                Hotdogs: Pollish, Frank, Chicken, Cheese
                Salad: Ceaser, Santa Fe, Thai, Garden
                Mac & Cheese: Regular, Extra Cheesy, Fried
                Soda: Coke, Pepsi, Sprite, Root Beer, Baja Blast
                Coffee: Black, Milk & Creamer, Latte, Americano, Mocha
                Tea: Black, Green, Olong, Lemon
                Juice: Orange Juice, Lemonaid, Grape Juice
                Milkshakes: Strawberry, Blueberry, Blackberry, Raspberry
                                                        """)

        lunch = input("What would you like to order? ")
        print("Your order is:" ,lunch)


    elif menuoption == "Dinner" or menuoption == "dinner":
        print("""
                    Here is our Dinner menu

                Cheesesteak: Steak or Chicken
                Egg Rolls: Chicken or Veggie
                Shrimp: Cocktail or Fried
                Half Meals: Burger & Fries, Chicken & Mash Potatoes
                Full Meals: I love Grease combo - Deep Fried Burger, Egg Rolls, Shrimp, Fries, & Onion Rings
                Soda: Coke, Pepsi, Sprite, Root Beer, Baja Blast
                Coffee: Black, Milk & Creamer, Latte, Americano, Mocha
                Tea: Black, Green, Olong, Lemon
                Juice: Orange Juice, Lemonaid, Grape Juice
                Milkshakes: Strawberry, Blueberry, Blackberry, Raspberry 
                                                        """)

        dinner = input("What would you like to order? ")
        print("Your order is:" ,dinner)

    else:
        print("Invalid Option. Please Choose Again")
        menu()

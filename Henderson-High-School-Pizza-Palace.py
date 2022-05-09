#Introduction
print("== HENDERSON HIGH SCHOOL PIZZA PALACE ==")
print("Welcome to Henderson High School Pizza Palace")

#Pizza Type
while True:
    pizza_type = input("Which pizza type would you like: \n A] Regular Pizza \n B] Gourmet Pizza \n Please select [A/B]:")
    if pizza_type == "A" or pizza_type == "a":
        print("Thank you, our regular pizza range is $8.50")
        break
    elif pizza_type == "B" or pizza_type == "b":
        print("Thank you, our gourmet pizza range is $13.50")
        break
    else:
        print("That is an invalid option. Please select [A/B]:")
        continue

#Pizza Menu
while True:
    if pizza_type == "A" or pizza_type == "a":
        regular_order=input("Our regular range of pizzas consist of: \n 1] Pepperoni \n 2] Cheese \n 3] Hawaiian \n 4] Meat Lovers \n 5] Sausage \n 6] Margherita \n 7] Vegetarian \n Please select [1, 2, 3, 4, 5, 6, 7]:")
        break
    if pizza_type == "B" or pizza_type == "b":
        gourmet_order=input("Our gourmet range of pizzas consist of: \n 1] Peri Peri Chicken \n 2] Apricot Chicken \n 3] MEGA Meatlovers \n 4] Chicken Cranberry \n 5] Fried Chicken & Bacon Ranch \n Please select [1, 2, 3, 4, 5, 6, 7]:")
        break

#Regular Order 1
while True:
    if regular_order == "1":
        print("Pepperoni!")
        break
    elif regular_order == "2":
        print("Cheese!")
        break
    elif regular_order == "3":
        print("Hawaiian!")
        break
    elif regular_order == "4":
        print("Meat Lovers!")
        break
    elif regular_order == "5":
        print("Sausage!")
        break
    elif regular_order == "6":
        print("Margherita!")
        break
    elif regular_order == "7":
        print("Vegetarian!")
        break
    else:
        print("That is an invalid option. \n Please select [A/B]:")
        continue

#Order Limit
while True: 
  pizza_limit = input("Would you like to add to your order? \n A] Yes \n B] No \n Please select [A/B]: ")
  break
  if pizza_limit == "A" or pizza_limit == "a" or pizza_limit == "Yes" or pizza_limit == "yes":
    print("REMEMBER YOU CAN SELECT UP TO FIVE PIZZAS")
  if pizza_limit == "B" or pizza_limit == "b" or pizza_limit == "No" or pizza_limit == "no":
    print("Thank you for your order! Before we start making your pizza we must collect your information.")

#Information Confirmation
print("Thank you for your order! \n Before we confirm your order we just need some more information")
name=input("What is your name:")
address=input("What is your address:")
number=input("What is your phone number:")
confirm=input("Name:", name,"\n Address:", address,"\n Phone Number:", number,"\n A] Yes \n B] No \n Please select [A/B]: ") 

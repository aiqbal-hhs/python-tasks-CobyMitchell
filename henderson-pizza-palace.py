#Lists
available_pizzas = ['Pepperoni', 'Cheese', 'Hawaiian', 'Meat Lovers', 'Sausage', 'Magherita', 'Vegetarian', 'Peri Peri Chicken', 'Apricot Chicken', 'MEGA Meat Lovers', 'Chicken Cranberry', 'Fried Chicken & Bacon Ranch']
available_toppings = ['Onions', 'Mushrooms', 'Black Olives', 'XTRA Cheese', 'XTRA Pepperoni']
pizza_prices = {'Pepperoni': 8.5, 'Cheese': 8.5, 'Hawaiian':8.5, 'Meat Lovers':8.5, 'Sausage':8.5, 'Magherita':8.5, 'Vegetarian': 8.5, 'Peri Peri Chicken':13.5, 'Apricot Chicken': 13.5, 'MEGA Meat Lovers': 13.5, 'Chicken Cranberry': 13.5, 'Fried Chicken & Bacon Ranch': 13.5}
topping_prices = {'Onions':0.5, 'Mushrooms':0.5, 'Black Olives':0.5, 'XTRA Cheese':0.5, 'XTRA Pepperoni':0.5}
sub_total = []
final_order = {}
customer_adress = {}


#Pizza Order
print("Welcome to Henderson High School Pizza Palace Phone Order Service")
order_pizza = True
while order_pizza:    
    print("Please Select A Pizza:")
    print()
    for pizzas in available_pizzas:
        print(pizzas)
        print()
    while True:
        pizza = input("What Pizza Would You Like To Order?")
        if pizza in available_pizzas:
            print(f"You Have Ordered A {pizza}.")
            sub_total.append(pizza_prices[pizza])
            break
        if pizza not in available_pizzas:
            print(f"Sorry, {pizza} Is Not In Stock.")

    #Extra Toppings
    order_topping = True
    print("Extra Toppings Menu")
    for toppings in available_toppings:
        print(toppings)
        print()
    while order_topping:
        extra_topping = input("Would You Like Any Extra Toppings? Yes or No?")
        if extra_topping == "Yes":
            topping = input("What Type Of Extra Toppings Would You Like?")
            if topping in available_toppings:
                final_order.setdefault(pizza, [])
                final_order[pizza].append(topping)
                print(f"{topping} has been added.")
                sub_total.append(topping_prices[topping])
            else:
                print(f"Sorry, We Do Not Have {topping} Currently In Stock.")

        elif extra_topping == "No":
            break
    extra_pizza = input("Would You Like To Order Another Pizza?")
    if extra_pizza == "No":
        for key, value in final_order.items():
            print(f"\nYou Have Order A {key} Pizza With {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is This Correct? Yes or No? ")
            if order_correct == "Yes":
                check_order = False
                order_pizza = False
            if order_correct == "No":
                print(final_order)
                add_remove = input("Would You Like To Add Or Remove? ")
                if add_remove == "Remove":
                    remove = input("Which Pizza Would You Like To Remove? ")
                    del final_order[remove]
                    print(final_order)
                if add_remove == "Add":
                    check_order = False

#Information Confirmation
    print("Would You Like Your Order Picked Up At Our Store or Delievered To Your Location?")
pickup_delievery=input("Please Select [Pickup] or [Delievery]:")
if pickup_delievery == "Pickup" or "pickup":                  
    print(f"\nYour total order price is: ${sum(sub_total)}")
if pickup_delievery == "Delievery" or "delievery":
    print(f"\nYour total order price is: ${sum(sub_total)} + $3 (For Delievery Cost)")
else:
    print("That Is An Invalid Option")

print("Before We Finalize Your Order We Need Your Name, Address and Phone Number:")
customer_adress['name'] = input("What Is Your Name?")
customer_adress['street_name'] = input("What Is Your Address?")
customer_adress['postalcode'] = input("What Is Your Postal Code and City?")
customer_adress['phonenumber'] = input("What Is Your Phone Number?")
print()
print(f"Thank You For Your Order {customer_adress['name']}.")
print()
print("Your Order Will Be Delievered To You ASAP")
print()
print(customer_adress['street_name'])
print(customer_adress['postalcode'])
print()
print(f"Our Team Will Contact Your For Any Inconvinence Of Your Order via {customer_adress['phonenumber']} If Anything Comes Up.")   
    

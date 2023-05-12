# from 4_1
pizzas = ["pepperoni", "margarita", "cheese"]
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("Pizza's great!")

#working with copy of list
friend_pizzas = pizzas[:]
pizzas.append("meat lovers")
friend_pizzas.append("veggie deluxe")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
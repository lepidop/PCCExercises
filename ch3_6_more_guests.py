#exercise 3_4
guests = ['rebecca sugar', 'ezra furman', 'john lennon'] 
print(f"m1: Dear {guests[0].title()}, you are invited to hayden's dinner.")
print(f"m2: Dear {guests[1].title()}, you are invited to hayden's dinner.")
print(f"m3: Dear {guests[2].title()}, you are invited to hayden's dinner.")
#exercise 3_5
print(f"{guests[2]} can't make it.")
guests[2] = "neil patrick harris"

print(f"m1: Dear {guests[0].title()}, you are invited to hayden's dinner.")
print(f"m2: Dear {guests[1].title()}, you are invited to hayden's dinner.")
print(f"m3: Dear {guests[2].title()}, you are invited to hayden's dinner.")
#exercise 3_6
print("A bigger dinner table has been found!")

guests.insert(0,"Bob Dylan")
guests.insert(2,"Alex Hirsch")
guests.append("Ursula K Le Guinn")

print(f"m1: Dear {guests[0].title()}, you are invited to hayden's dinner.")
print(f"m2: Dear {guests[1].title()}, you are invited to hayden's dinner.")
print(f"m3: Dear {guests[2].title()}, you are invited to hayden's dinner.")
print(f"m4: Dear {guests[3].title()}, you are invited to hayden's dinner.")
print(f"m5: Dear {guests[4].title()}, you are invited to hayden's dinner.")
print(f"m6: Dear {guests[5].title()}, you are invited to hayden's dinner.")
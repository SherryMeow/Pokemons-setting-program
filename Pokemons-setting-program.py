pokemon_names = ['Charmander', 'Squirtle', 'Bulbasaur', 'Gyrados']
pokemon_counts = [3, 2, 5, 1]
pokemon_fees = [100.0, 50.0, 25.0, 1000.0]
pokemon_types = [['Fire'], ['Water'], ['Grass'], ['Water', 'Flying']]
valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']
def search_by_name():
    name = input("Name of Pokemon to search for: ").title()
    if name in pokemon_names:
        index = pokemon_names.index(name)
        count = pokemon_counts[index]
        fee = pokemon_fees[index]
        types = pokemon_types[index]
        print(f"We have {count} {name} at the Pokemon Center")
        print(f"It will cost ${fee:,.2f} to adopt this Pokemon")
        print(f"{name} has the following types: {', '.join(types)}\n")
    else:
        print(f"Sorry, we don't have any {name} at the Pokemon Center\n")

def search_by_type():
    type_name = input("Enter Pokemon type: ").title()
    found = False
    print("{:<20}{:>20}{:>20} {:<20}".format('Name', 'Amount Available', 'Adoption Fee', 'Type(s)'))
    for i in range(len(pokemon_names)):
        types = pokemon_types[i]
        if type_name in types:
            found = True
            name = pokemon_names[i]
            count = pokemon_counts[i]
            fee = pokemon_fees[i]
            print("{:<20}{:>20}{:>20} {:<20}".format(name, count, f"{fee:,.2f}", ', '.join(types)))
    if not found:
        print("We have no Pokemon of that type at our Pokemon Center")
    print()




def list_pokemon():
    print("{:<20}{:>20}{:>20} {:<20}".format('Name', 'Amount Available', 'Adoption Fee', 'Type(s)'))
    for i in range(len(pokemon_names)):
        name = pokemon_names[i]
        count = pokemon_counts[i]
        fee = pokemon_fees[i]
        types = pokemon_types[i]
        print("{:<20}{:>20}{:>20} {:<20}".format(name, count, f"{fee:,.2f}", ', '.join(types)))
    print()

print("Welcome to the Pokemon Center!")

valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

def add_pokemon():
    name = input("Enter name of new pokemon: ").title()
    if name in pokemon_names:
        print("Duplicate name, add operation cancelled\n")
        return

    while True:
        count = int(input("How many of these Pokemon are you adding? "))
        if count > 0:
            break
        else:
            print("Invalid, please try again")

    while True:
        fee = float(input("What is the adoption fee for this Pokemon? "))
        if fee > 0:
            break
        else:
            print("Invalid, please try again")

    types = []
    print("Next you will be prompted to enter the 'types' for this Pokemon. Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")
    while True:
        type_name = input("What type of Pokemon is this? ").lower()
        if type_name == 'help':
            print('* ' + '\n* '.join(valid_pokemon_types))
        elif type_name == 'end':
            if len(types) > 0:
                break
            else:
                print("You must enter at least one valid 'type'")
        elif type_name in valid_pokemon_types:
            if type_name not in types:
                types.append(type_name.title())
                print(f"Type {type_name.title()} added")
            else:
                print("This type has already been added")
        else:
            print("This is not a valid type, please try again")

    pokemon_names.append(name)
    pokemon_counts.append(count)
    pokemon_fees.append(fee)
    pokemon_types.append(types)
    print("Pokemon Added!\n")

def remove_pokemon():
    name = input("Enter name of Pokemon to remove: ").title()
    if name in pokemon_names:
        index = pokemon_names.index(name)
        del pokemon_names[index]
        del pokemon_counts[index]
        del pokemon_fees[index]
        del pokemon_types[index]
        print("Pokemon removed\n")
    else:
        print("Pokemon not found, cannot remove\n")

def report():
    highest_price = max(pokemon_fees)
    highest_price_index = pokemon_fees.index(highest_price)
    lowest_price = min(pokemon_fees)
    lowest_price_index = pokemon_fees.index(lowest_price)
    total_cost = sum([pokemon_counts[i] * pokemon_fees[i] for i in range(len(pokemon_counts))])

    print(f"Highest priced Pokemon: {pokemon_names[highest_price_index]} @ ${highest_price:,.2f} per Pokemon")
    print(f"Lowest priced Pokemon: {pokemon_names[lowest_price_index]} @ ${lowest_price:,.2f} per Pokemon")
    print(f"Total cost to adopt all Pokemon in the Center: ${total_cost:,.2f}\n")

while True:
    action = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ").lower()
    if action == 'a':
        add_pokemon()
    elif action == 'r':
        remove_pokemon()
    elif action == 'e':
        report()
    elif action == 's':
        search_by_name()
    elif action == 't':
        search_by_type()
    elif action == 'l':
        list_pokemon()
    elif action == 'q':
        print("See you next time!")
        break
    else:
        print("Sorry, that's not a valid action. Please try again.\n")

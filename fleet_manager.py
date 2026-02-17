def init_database():

    names = ["Jones", "Smith", "Matthews"]
    ranks = ["Captain", "Commander", "lieutenant"]
    divisions = ["Command", "Operations", "Safety"]
    crew_ids = ["1", "2", "3"]

    return names, ranks, divisions, crew_ids

names, ranks, divisions, crew_ids = init_database()

print(names)
print(ranks)
print(divisions)
print(crew_ids)

def display_menu(student_name):
    print("\n--- Fleet Manager ---")
    print("Logged in as:", student_name)
    print("1 - Display crew")
    print("2 - Add member")
    print("3 - Remove member")
    print("4 - Update rank")
    print("5 - Search Crew")
    print("6 - Filter by division")
    print("7 - Calculate payroll")
    print("8 - Count Senior Officers")
    print("9 - Exit")

    choice = input("Choose option: ")
    return choice

def display_roster(names, ranks, divisions, crew_ids):
    print("\nCrew List:\n")

    for i in range(len(names)):
        print("Name:", names[i])
        print("Rank:", ranks[i])
        print("Division:", divisions[i])
        print("ID:", crew_ids[i])
        print()

def add_member(names, ranks, divisions, crew_ids):
    name = input("Enter name: ")
    rank = input("Enter rank: ")
    division = input("Enter division: ")
    crew_id = input("Enter ID: ")

    names.append(name)
    ranks.append(rank)
    divisions.append(division)
    crew_ids.append(crew_id)

    print("Member added successfully ")

def remove_member(names, ranks, divisions, crew_ids):
    crew_id = input("Enter ID to remove: ")

    if crew_id in crew_ids:
        i = crew_ids.index(crew_id)
        names.pop(i)
        ranks.pop(i)
        divisions.pop(i)
        crew_ids.pop(i)
        print("Member removed ")
    else:
        print("ID not found ")

def update_rank(names, ranks, crew_ids):
    crew_id = input("Enter ID: ")

    if crew_id in crew_ids:
        i = crew_ids.index(crew_id)
        new_rank = input("Enter new rank: ")
        ranks[i] = new_rank
        print("Rank updated ")
    else:
        print("ID not found ")

def search_crew(names, ranks, divisions, crew_ids):
    name = input("Enter name: ")

    for i in range(len(names)):
        if names[i].lower() == name.lower():
            print(names[i], ranks[i], divisions[i], crew_ids[i])
            return
        
        print("Not found")

while True:
    choice = display_menu("Shivani")

    if choice == "1":
        display_roster(names, ranks, divisions, crew_ids)

    elif choice == "2":
        add_member(names, ranks, divisions, crew_ids)

    elif choice == "3":
        remove_member(names, ranks, divisions, crew_ids)

    elif choice == "4":
        update_rank(names, ranks, crew_ids)

    elif choice == "5":
        search_crew(names, ranks, divisions, crew_ids)

    elif choice == "9":
        print("Exit program")
        break

    else:
        print("Option not implemented yet")
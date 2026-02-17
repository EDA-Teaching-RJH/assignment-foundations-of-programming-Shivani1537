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

display_menu("Shivani")
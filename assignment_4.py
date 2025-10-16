'''
Thea Labuntog thl1733@rit.edu
ISCH-620 Assignment 4: Working with Lists, Tuples, and Sets (Dinosaurs)
GenAI Statement: I used ChatGPT on how to outline tuples. I wrote the code and comments myself based on the outline.
'''

# --- input validation ---
def is_valid_choice(choice):
    # check if the user's menu choice is valid (1-4 or Q/q to quit)
    return choice in ['1', '2', '3', '4', 'q', 'Q']

def is_valid_dinosaur(choice):
    # check if the input is a valid dinosaur from list of options
    return choice in ['Tyrannosaurus', 'Velociraptor', 'Triceratops', 'Brachiosaurus', 'Stegosaurus']

def is_valid_index(index, collection):
    # check if the input index is valid (0, 1, or 2)
    if not str(index).isdigit(): # input has to be a digit!
        print("Please choose between 0, 1, or 2.")
        return index in ['0', '1', '2']
    index = int(index)
    return 0 <= index < len(collection) # check if index is within bounds of collection since it's zero-based indexing

def get_valid_dinosaur(prompt = "Enter a dinosaur name (or 'Q/q' to quit): "):
    while True:
        name = input(prompt).strip().title() # normalize input to title case and remove extra spaces
        if name.lower() == 'q':
            return None
        if is_valid_dinosaur(name):
            return name
        print("Invalid dinosaur name. Please select from the options: Tyrannosaurus, Velociraptor, Triceratops, Brachiosaurus, Stegosaurus.")

# --- option 1: python concepts ---
def show_definitions():
    print("\nImportant Python Concepts:")
    print("Iterable: An object capable of returning its members one at a time. Examples include lists, tuples, and sets!")
    print("Non-iterable: An object that cannot be iterated over, such as integers and floats.")
    print("Mutable: An object that can be changed after its creation (ex. lists).")
    print("Immutable: An object that cannot be changed after its creation (ex. tuples).")
    print("Index: A numerical representation of an item's position in an ordered collection, starting from 0.")
    print("List: A mutable (changeable), ordered collection of items. You can add, remove, or change items.")
    print("Tuple: An immutable (unchangeable), ordered collection of items. Once created, you cannot change it.")
    print("Set: An unordered collection of unique items. It does not allow duplicates and does not maintain order.")
    print("-----------------------------------")


# --- option 2: list ---
def work_with_list():
    print("\nWorking with a List:")
    print("List: A mutable (changeable), ordered collection of items. You can add, remove, or change items.")

    dinosaur_list = []
    print("AVAILABLE DINOS: Tyrannosaurus, Velociraptor, Triceratops, Brachiosaurus, Stegosaurus")
    print("Enter up to three dinosaur names to add to the list (or 'Q/q' to quit): ")
    print("NOTE: List: A mutable (changeable), ordered collection of items. You can add, remove, or change items. Enter one dinosaur name at a time!")
    print("----------------🦖-------------------")

    for i in range(3):  # using range to limit to 3 entries
        remaining = 3 - len(dinosaur_list)
        prompt = f"Enter dinosaur name ({remaining} slots left), or 'Q/q' to finish: "
        name = get_valid_dinosaur(prompt)
        if name is None: # if user chose to quit
            break
        dinosaur_list.append(name)
        print(f"Current List: {dinosaur_list}")

    if not dinosaur_list:
        print("Oh no! No dinosaurs were entered 🦖.")
        return

    print("\nIterating through the list by index using range():") # index selection 
    for i in range(len(dinosaur_list)):
        print(f"Index {i}: {dinosaur_list[i]}")

    print("\nIterating through the list by value:")
    for dino in dinosaur_list:
        print(f"Dinosaur: {dino}")

    while True:
        index = input("\nSelect a dinosaur by its index (0, 1, or 2) or 'Q/q' to quit: ")
        if index == 'q' or index == 'Q':
            return
        if not is_valid_index(index, dinosaur_list):
            print(f"Oh no! Please enter a valid index (0, 1, or 2) based on your list: {dinosaur_list}")
            continue
        index = int(index)
        print(f"You selected: {dinosaur_list[index]}!")


# --- option 3: tuple ---
def work_with_tuple():
    print("\nWorking with a Tuple:")
    print("Tuple: An immutable (unchangeable), ordered collection of items. Once created, you cannot change it.")

    dino_tuple_list = []
    print("AVAILABLE DINOS: Tyrannosaurus, Velociraptor, Triceratops, Brachiosaurus, Stegosaurus")
    print("Enter up to three dinosaur names to add to the tuple (or 'Q/q' to quit): ")
    print("NOTE: Tuple: An immutable (unchangeable), ordered collection of items. Once created, you cannot change it. Enter one dinosaur name at a time!")
    print("----------------🦖-------------------")

    while len(dino_tuple_list) < 3:
        name = get_valid_dinosaur(f"Enter a dinosaur name to add ({3-len(dino_tuple_list)} left) or 'Q' to finish: ")
        if name is None: 
            break
        dino_tuple_list.append(name)

    dinosaur_tuple = tuple(dino_tuple_list)

    if not dinosaur_tuple:
        print("Oh no! No dinosaurs were entered 🦖.")
        return
    
    print("\nIterating through the tuple using range():") # iterate through tuple using range()
    for i in range(len(dinosaur_tuple)):
        print (f"Index {i}: {dinosaur_tuple[i]}")

    while True:
        index = input("\nSelect a dinosaur by its index (0, 1, or 2) or 'Q/q' to quit: ")
        if index == 'q' or index == 'Q':
            return
        if not is_valid_index(index, dinosaur_tuple):
            print(f"Oh no! Please enter a valid index (0, 1, or 2) based on your tuple: {dinosaur_tuple}")
            continue
        index = int(index)
        print(f"You selected: {dinosaur_tuple[index]}!")

        
# --- option 4: set ---
def work_with_set():
    dinosaur_set = set()
    print("\nWorking with a Set:")
    print("Set: An unordered collection of unique items. It does not allow duplicates and does not maintain order.")

    dinosaur_set = set()
    print("AVAILABLE DINOS: Tyrannosaurus, Velociraptor, Triceratops, Brachiosaurus, Stegosaurus")
    print("Enter up to three dinosaur names to add to the set (or 'Q/q' to quit): ")
    print("NOTE: Set: An unordered collection of unique items. It does not allow duplicates and does not maintain order. Enter one dinosaur name at a time!")
    print("----------------🦖-------------------")

    while len(dinosaur_set) < 3:
        name = get_valid_dinosaur(f"Enter a dinosaur name to add ({3-len(dinosaur_set)} left) or 'Q' to finish: ")
        if name is None:
            break
        if name in dinosaur_set:
            print(f"{name} already in set; sets ignore duplicates.") # ignore duplicates
            continue
        dinosaur_set.add(name)
        print(f"Current Set: {dinosaur_set}")

    if not dinosaur_set:
        print("Oh no! No dinosaurs were entered 🦖.")
        return

    # iterate through set (no indexing; no indexing in sets, so we can't select by index!!)
    print("\nIterating through the set (note: sets are unordered, so order may vary):")
    for dino in dinosaur_set:
        print(dino)

    # --- allow selection by typing in a dinosaur name
    while True:
        selected_dino = input("Select a dinosaur by typing its name or 'Q/q' to quit: ")
        if selected_dino == 'q' or selected_dino == 'Q':
            return
        if not is_valid_dinosaur(selected_dino):
            print("Oh no! Please select from the dinosaur options 🦖.")
            continue
        if selected_dino in dinosaur_set:
            print(f"You selected: {selected_dino}!")
        else:
            print("Dinosaur not found in the set.")


# --- greeting and menu ---
def main():
    print("Hello! Welcome to the Dinosaur Program 🦖🦕.")
    print("This program lets you explore Python iterable types (lists, tuples, and sets) using dinosaur names.")
    print("You can input up to three names and see how each type behaves. To learn more, check out important Python concepts.")
    print("To exit, enter 'Q/q'.")

    # menu Loop
    while True:
        print("\nMenu:")
        print("1. Important Python Concepts")
        print("2. Work with a List")
        print("3. Work with a Tuple")
        print("4. Work with a Set")
        print("q. Quit")

        choice = input("Please select an option (1-4) or 'Q/q' to quit: ")

        if choice == 'q' or choice == 'Q':
            print("Exiting the Dinosaur Data Program 🦖🦕. Goodbye!")
            break
        elif is_valid_choice(choice):
            print("\n-----------------------------------")
            print(f"You selected option {choice}.")
            if choice == "1":
                print("You chose Option 1: Important Python Concepts.")
                show_definitions()
            elif choice == "2":
                print("You chose Option 2: Working with Lists.")
                work_with_list()
            elif choice == "3":
                print("You chose Option 3: Working with Tuples.")
                work_with_tuple()
            elif choice == "4":
                print("You chose Option 4: Working with Sets.")
                work_with_set()
            else:
                print("Don't have that option! Please try again, or Q/q to quit.")

if __name__ == "__main__":
    main()
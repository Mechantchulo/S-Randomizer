import random
import datetime
import os

# File Paths
DISHES_FILE = 'dishes.txt'
HISTORY_FILE = 'history.txt'

# Default Dish List
DEFAULT_DISHES = [
    'Ugali na Sukuma Wiki',
    'Ugali na Cabbage',
    'Pilau',
    'Githeri',
    'Ugali-Mayai',
    'Rice-beans',
    'Indomie',
    'Chapati-beans',
    'Fruit salad',
    'Chips'
]

# Load Dishes
def load_dishes():

    with open(DISHES_FILE, 'r') as file:
        dishes = [line.strip() for line in file.readlines() if line.strip()]
    return dishes

# Save Dishes
def save_dishes(dishes):
    with open(DISHES_FILE, 'w') as file:
        file.write("\n".join(dishes))

# Load History
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return None, None
    with open(HISTORY_FILE, 'r') as file:
        last_dish, last_date = file.read().strip().split('|')
    return last_dish, datetime.datetime.strptime(last_date, '%Y-%m-%d').date()

# Save History
def save_history(dish):
    with open(HISTORY_FILE, 'w') as file:
        file.write(f'{dish}|{datetime.date.today()}')

# Get Random Dish
def get_random_dish():
    dishes = load_dishes()
    last_dish, last_date = load_history()
    if last_date and (datetime.date.today() - last_date).days < 7:
        choices = [dish for dish in dishes if dish != last_dish]
    else:
        choices = dishes
    chosen_dish = random.choice(choices) if choices else 'No dishes available!'
    save_history(chosen_dish)
    return chosen_dish

# Add Dish
def add_dish():
    new_dish = input("Enter new dish name: ").strip()
    dishes = load_dishes()
    if new_dish and new_dish not in dishes:
        dishes.append(new_dish)
        save_dishes(dishes)
        print(f"{new_dish} added.")
    else:
        print("Dish already exists or is invalid.")

# Remove Dish
def remove_dish():
    dishes = load_dishes()
    print("Current Dishes:")
    for i, dish in enumerate(dishes, 1):
        print(f"{i}. {dish}")
    try:
        choice = int(input("Enter number to remove: ")) - 1
        if 0 <= choice < len(dishes):
            removed = dishes.pop(choice)
            save_dishes(dishes)
            print(f"{removed} removed.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")

# View Dishes
def view_dishes():
    dishes = load_dishes()
    print("Current Dishes:")
    for dish in dishes:
        print(f"- {dish}")

# View History
def view_history():
    last_dish, last_date = load_history()
    if last_dish:
        print(f"Last Dish: {last_dish} on {last_date}")
    else:
        print("No history available.")

# Reset History
def reset_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    print("History reset.")

# Main Menu
def main_menu():
    while True:
        print("\nErick's Supper Randomizer")
        print("1. Get Today's Random Dish")
        print("2. Add Dish")
        print("3. Remove Dish")
        print("4. View Dishes")
        print("5. View History")
        print("6. Reset History")
        print("7. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            print("Today's Dish: ", get_random_dish())
        elif choice == '2':
            add_dish()
        elif choice == '3':
            remove_dish()
        elif choice == '4':
            view_dishes()
        elif choice == '5':
            view_history()
        elif choice == '6':
            reset_history()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main_menu()

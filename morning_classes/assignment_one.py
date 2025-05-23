def display_menu():
    """Display the main menu options"""
    print("\nInventory Management System")
    print("*************MENU*************")
    print("Select an option:")
    print("1. View all items")
    print("2. Add new item")
    print("3. Update item quantity")
    print("4. Delete item")
    print("5. Exit")

def view_inventory(inventory):
    """Display all items in inventory"""
    print("\nCurrent Inventory:")
    print("-" * 30)
    print(f"{'ID':<5}{'Item':<15}{'Quantity':<10}{'Price':<10}")
    print("-" * 30)
    for item_id, item in inventory.items():
        print(f"{item_id:<5}{item['name']:<15}{item['quantity']:<10}${item['price']:.2f}")

def add_item(inventory):
    """Add a new item to inventory"""
    print("\nAdd New Item")
    name = input("Enter item name: ")
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: $"))
            break
        except ValueError:
            print("Please enter valid numbers for quantity and price")
    
    # Generate new ID (max existing ID + 1)
    new_id = max(inventory.keys()) + 1 if inventory else 1
    inventory[new_id] = {
        'name': name,
        'quantity': quantity,
        'price': price
    }
    print(f"Item '{name}' added with ID {new_id}")

def update_item(inventory):
    """Update quantity of an existing item"""
    view_inventory(inventory)
    try:
        item_id = int(input("\nEnter ID of item to update: "))
        if item_id not in inventory:
            print("Error: Invalid ID")
            return
        
        print(f"\nUpdating {inventory[item_id]['name']}")
        while True:
            try:
                new_quantity = int(input("Enter new quantity: "))
                new_price = float(input("Enter new price: $"))
                break
            except ValueError:
                print("Please enter valid numbers")
        
        inventory[item_id]['quantity'] = new_quantity
        inventory[item_id]['price'] = new_price
        print("Item updated successfully")
    except ValueError:
        print("Please enter a valid ID number")

def delete_item(inventory):
    """Remove an item from inventory"""
    view_inventory(inventory)
    try:
        item_id = int(input("\nEnter ID of item to delete: "))
        if item_id not in inventory:
            print("Error: Invalid ID")
            return
        
        item_name = inventory[item_id]['name']
        del inventory[item_id]
        print(f"Item '{item_name}' (ID: {item_id}) deleted")
    except ValueError:
        print("Please enter a valid ID number")

def main():
    """Main program loop"""
    # Sample initial inventory
    inventory = {
        1: {'name': 'Keyboard', 'quantity': 50, 'price': 29.99},
        2: {'name': 'Mouse', 'quantity': 75, 'price': 19.99},
        3: {'name': 'Monitor', 'quantity': 20, 'price': 199.99}
    }
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            view_inventory(inventory)
        elif choice == '2':
            add_item(inventory)
        elif choice == '3':
            update_item(inventory)
        elif choice == '4':
            delete_item(inventory)
        elif choice == '5':
            print("Exiting inventory system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5")

if __name__ == "__main__":
    main()
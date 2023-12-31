class inventoryManagement:
    def __init__(self):
        self.inventory={}

    def display_menu(self):
        print("\nInventory Management System\n")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Quantity")
        print("5. Set Minimum Stock Level")
        print("6. Exit")

    def view_inventory(self):
        
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:\n")
            print("{:<15} {:<10} {:<10} {:<10}".format("Item","Quantity","Min.Stock","Status"))
            for item,details in self.inventory.items():
                status = "OK" if details["quantity"]>=details["min_stock"] else "Low Stock"
                print("{:<15} {:<10} {:<10} {:<10}".format(item,details["quantity"],details["min_stock"],status))

    def add_item(self):
        item_name=input("Enter item name: ")
        quantity=int(input("Enter quantity: "))
        min_stock=int(input("Enter minimum stock level: "))

        if item_name not in self.inventory:
            self.inventory[item_name]={"quantity": quantity,"min_stock": min_stock}
            print(f"Item '{item_name}' added to the inventory.")
        else:
            print(f"Item '{item_name}' already exists.")

    def remove_item(self):
        item_name = input("Enter the item name to remove: ")
        
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"Item '{item_name}' removed from the inventory.")
        else:
            print(f"Item '{item_name}' not found in the inventory.")

    def update_quantity(self):
        item_name = input("Enter the item name to update quantity: ")
        
        if item_name in self.inventory:
            quantity=int(input("Enter the updated quantity: "))
            self.inventory[item_name]["quantity"]=quantity
            print(f"Quantity for item '{item_name}' updated to {quantity}.")
        else:
            print(f"Item '{item_name}' not found in the inventory.")

    def set_min_stock_level(self):
        item_name=input("Enter the item name to set minimum stock level: ")
        
        if item_name in self.inventory:
            min_stock=int(input("Enter the minimum stock level: "))
            self.inventory[item_name]["min_stock"] = min_stock
            print(f"Minimum stock level for item '{item_name}' set to {min_stock}.")
        else:
            print(f"Item '{item_name}' not found in the inventory.")

    def main(self):
        
        while True:
            self.display_menu()
            choice=input("\nEnter your choice (1-6): ")

            if choice=='1':
                self.view_inventory()
            elif choice=='2':
                self.add_item()
            elif choice=='3':
                self.remove_item()
            elif choice=='4':
                self.update_quantity()
            elif choice=='5':
                self.set_min_stock_level()
            elif choice=='6':
                print("Thank You")
                break
            else:
                print("Invalid choice.Please enter a number between 1 and 6.")

if __name__=="__main__":
    inventoryManagement().main()

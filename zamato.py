class ZomatoSystem:
    def __init__(self):
        self.dishes = [
            {"ID": 1, "Name": "samosa", "Quantity": 10, "Price": 20},
            {"ID": 2, "Name": "momo", "Quantity": 5, "Price": 10},
            {"ID": 3, "Name": "pizza", "Quantity": 8, "Price": 100}
        ]
        self.orders = []
    
    def show_menu(self):
        print("\nMenu:")
        for dish in self.dishes:
            print(dish)
        print()
    
    def add_dish(self):
        name = input("Enter Dish Name: ")
        Id = int(input("Enter Dish ID: "))
        price = int(input("Enter Dish Price: "))
        quantity = int(input("Enter Dish Quantity: "))
        
        for dish in self.dishes:
            if dish["ID"] == Id:
                print("\nDish already exists with this ID.\n")
                return
        
        new_dish = {"ID": Id, "Name": name, "Price": price, "Quantity": quantity}
        self.dishes.append(new_dish)
        print("\nDish Added Successfully.\n")
    
    def remove_dish(self):
        Id = int(input("Enter Dish ID: "))
        
        for dish in self.dishes:
            if dish["ID"] == Id:
                self.dishes.remove(dish)
                print("\nDish Removed Successfully.\n")
                return
        
        print("\nItem doesn't exist.\n")
    
    def update_availability(self):
        Id = int(input("Enter Dish ID: "))
        Inc = int(input("Enter Quantity You want to increase: "))
        
        for dish in self.dishes:
            if dish["ID"] == Id:
                dish["Quantity"] += Inc
                print("\nQuantity Increased Successfully.\n")
                return
        
        print("\nDish with this ID doesn't exist.\n")
    
    def new_order(self):
        name = input("Enter your Name: ")
        Id = int(input("Enter Dish ID: "))
        quantity = int(input("Enter Quantity: "))
        
        for dish in self.dishes:
            if dish["ID"] == Id and dish["Quantity"] >= quantity:
                dish["Quantity"] -= quantity
                order = {
                    "Name": name,
                    "ID": Id,
                    "Dish": dish["Name"],
                    "Price": dish["Price"] * quantity,
                    "Status": "received"
                }
                self.orders.append(order)
                print("\nOrder placed successfully.\n")
                return
        
        print("\nItem is out of stock or doesn't exist.\n")
    
    def update_order_status(self):
        Id = int(input("Enter Order ID: "))
        
        for order in self.orders:
            if order["ID"] == Id:
                order["Status"] = "prepared"
                print("\nOrder status changed successfully.\n")
                return
        
        print("\nOrder with this ID doesn't exist.\n")
    
    def review_orders(self):
        print("\nOrders:")
        for order in self.orders:
            print(order)
        print()
    
    def run(self):
        while True:
            print("Welcome to Zesty Zomato")
            print("Choose an option:")
            print("1. Show Menu")
            print("2. Add Dish")
            print("3. Remove Dish")
            print("4. Update Availability")
            print("5. New Order")
            print("6. Update Order Status")
            print("7. Review Orders")
            print("8. Exit")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                self.show_menu()
            elif choice == 2:
                self.add_dish()
            elif choice == 3:
                self.remove_dish()
            elif choice == 4:
                self.update_availability()
            elif choice == 5:
                self.new_order()
            elif choice == 6:
                self.update_order_status()
            elif choice == 7:
                self.review_orders()
            elif choice == 8:
                print("Exiting. Have a great day!")
                break
            else:
                print("Invalid choice. Please select a valid option.\n")


if __name__ == "__main__":
    system = ZomatoSystem()
    system.run()

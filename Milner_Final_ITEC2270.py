# Frankie Milner 
# July 19th, 2023
# July 21st, 2023
# Final Project 
# Simple online car buying system to register cars and buy them 

print("\nThis program will register new cars and customers for car purchasing")
# define the class as car and initialize the self and the constructor 
class Car():
    def __init__(a, registration, make, model, type, year, mileage, color, price):
        a.registration = registration.title()
        a.make = make.title()
        a.model = model.title()
        a.type = type.title()
        a.year = year.title()
        a.mileage = mileage.title()
        a.color = color.title()
        a.price = price.title()

    # Get the attributes and set registration ID number  
    def get_registration(a):
        return a.registration
    def set_registration(a):
        a.registration = float()
    
    # Get the attributes and set model
    def get_model(a): 
        return a.model
    def set_model(a):
        a.model = str()
    
    # Get the attributes and set type
    def get_type(a): 
        return a.type
    def set_type(a):
        a.type = str()

    # Get the attributes and set year
    def get_year(a): 
        return a.year
    def set_year(a):
        a.year = int()

    # Get the attributes and set mileage
    def get_mileage(a): 
        return a.mileage
    def set_mileage(a):
        a.mileage = int()

    # Get the attributes and set color
    def get_color(a): 
        return a.color
    def set_color(a):
        a.color = str()
    
    # Get the attributes and set price
    def get_price(a):
        return a.price
    def set_price(a):
        a.price = float()

class Customer(): 
    def __init__(a, ID, name, address, email, telephone):
        a.ID = ID.title()
        a.name = name.title()
        a.address = address.title()
        a.email = email.title()
        a.telephone = telephone.title()

        # Get the attributes and set customer ID number  
    def get_ID(a):
        return a.ID
    def set_ID(a):
        a.ID = float()
    
    # Get the attributes and set customer name 
    def get_name(a): 
        return a.name
    def set_name(a):
        a.name = str()
    
    # Get the attributes and customer address 
    def get_address(a): 
        return a.address
    def set_address(a):
        a.address = str()

    # Get the attributes and set customer email address 
    def get_email(a): 
        return a.email
    def set_email(a):
        a.email = str()

    # Get the attributes and set customer telephone number 
    def get_telephone(a): 
        return a.telephone
    def set_telephone(a):
        a.telephone = int()


def main(): 
    vehicle_list = [registration, make, model, type, year, mileage, color, price]
    vehicle = Car(registration, make, model, type, year, mileage, color, price)
    customer_list = [ID, name, address, email, telephone]
    customer = Customer(ID, name, address, email, telephone)

# Once the attributes are set, create menu function to get car & guest details    
def menu(): 
    print("[1] Add Vehicle to Inventory")
    print("[2] Delete Vehicle from Inventory")
    print("[3] View Inventory ")
    print("[4] Add Customer")
    print("[5] Delete a Customer")
    print("[6] Buy a car")
    print("[7] View Customer Database")
    print("[0] Exit the Program")

menu()
option = int(input("Enter your option: "))
# while and if/else decision structure to go through menu options 
while option !=0:
    if option == 1: 
        f = open("Vehicle_Registry.txt", "a")
        registration = input("Enter the registration ID number: ")
        make = input("Please enter make: ")
        model = input("Please enter model: ")
        type = input("Please enter type: ")
        year = input("Please enter year: ")
        mileage = input("Please enter mileage: ")
        color = input("Please enter color: ")
        price = input("Please enter price: ")
        vehicle_list = [registration, make, model, type, year, mileage, color, price]
        n_vehicle_list = ["{}\n".format(i) for i in vehicle_list]
        f.writelines(n_vehicle_list)
        #print(registration, make, model, type, year, mileage, color, price)
        f.close()
    elif option == 2: # Delete Vehicle from Inventory 
        f = open("Vehicle_Registry.txt", 'w')
        f.close()
        print("The vehicle was removed!")
    elif option == 3: #View Inventory 
            f = open("Vehicle_Registry.txt", "r")
            print(f.read())
            f.close()
    elif option == 4: # Add Customer 
        f2 = open("Customer_Registry.txt", "a")
        ID = input("Please enter customer ID: ")
        name = input("Please enter customer name: ")
        address = input("Please enter customer address: ")
        email = input("Please enter customer email address: ")
        telephone = input("Please enter customer telephone number: ")
        customer_list = [ID, name, address, email, telephone]
        n_customer_list = ["{}\n".format(i) for i in customer_list]
        f2.writelines(n_customer_list)
        f2.close()
    elif option == 5: # Delete a customer 
        f2 = open("Customer_Registry.txt", 'w')
        f2.close()
        print("This customer has been removed from our database!")
    elif option == 6: # Buy a car 
        print("\nCongratulations, you want to buy a car!")
        car_price = int(input("Please enter the price of the vehicle: "))
        down_payment = int(input("Please enter the down payment amount: "))
        loan_term = int(input("Please enter the loan term time period(months): "))
        monthly = (car_price - down_payment) / loan_term
        print("The monthly payment will be", + monthly)
    elif option == 7: # View Customer Database
        f2 = open("Customer_Registry.txt", 'r')
        print(f2.read())
        f2.close()
    else: # Invalid option other than 0-7
        print("Invalid option!")

    print()
    menu()
    option = int(input("Enter your option: "))

print("\nThanks for using Frankie's Autogram!")

if __name__ == "__main__":
    main()
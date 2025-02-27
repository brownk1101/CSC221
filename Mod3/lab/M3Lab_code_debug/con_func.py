from m3Lab_classes import Customer
    
def menu():
    #Display the header
    print("Menu")
    print("----------------")
    print("1. Display Customer Dataset" 
          + "\n2. Add Customer"
          + "\n3. Update Customer Info"
          + "\n4. Exit Program and Generate Customer Files")

def get_cusInfo():
    """Read csv file of customers and create Customer Instances

    Returns
    -------
    customers : List of Customer Instances.
    """
    
    customers = []


    with open(file="customer.csv", mode="r", encoding="utf8") as customer_file:
        # Skip header row.
        next(customer_file)
        # Read the rest of the file by rows.
        for row in customer_file:
            # Extract user information
            first, last, phone, email, state, address = row.strip().split(",")
            # Create and append the customer object to the list.
            customers.append(Customer(first, last, phone, email, state, address))

    return customers

    
def cus_update(lastName, customers):
    """Update phone or address of customer.

    Parameters
    ----------
    lastName: str
        Last name of customer to update.
    customers: list[Customer]
        List of customer objects.

    Returns
    -------
    list[Customer]
        Returns updated list if the customer is found, the same list if not found,
        or None if the submenu choice isn't correct.
    """

    found = False 
                
    for cus in customers:
        
        cus_last = cus.get_last()
        
        # check if instance last name is same as one we want to update
        if cus_last == lastName: # customer found in list
            cus_first = cus.get_first()
            cus_address = cus.get_address()
            cus_phone = cus.get_phone()

            found = True
            
            # ask user to choose from update options
            print("\nWhat would you like to update? ")
            print("\n1) Update Phone")
            print("2) Update Address")
            print()
            
            option = input("Enter choice: ")
            try:
                option = int(option)
            except ValueError:
                # The else clause will handle invalid input.
                pass

            # see option picked
            if option == 1: # update phone
                # display old phone number
                print()
                print(cus_first + " " + cus_last + " current phone number is " + cus_phone)
                
                # get new phone number
                phone = input("What is " + cus_first + " " + cus_last + "\'s new phone number? ")
                
                # update the phone
                cus.set_phone(phone)
                # show new information to user
                print("\nPhone number updated, see below\n")
                print(cus_first + cus_last + " updated phone number is " + cus_phone)
                
                return customers # return updated customers list
            
            elif option == 2: # update address
                
                # display old address
                print()
                print(cus_first + cus_last + " current address is " + cus_address)
                
                # ask if moving to new state
                move = input("Will " + cus_first + " " + cus_last + " be moving to a new state(y for yes)?  ")
                
                if move.lower() =="y":
                    # get state
                    state = input("Enter the state " + cus_first + " " + cus_last + " will move to: ")     
                
                    # get new address
                    address = input("What is " + cus_first + " " + cus_last + "\'s new address? ")
                    
                    #update
                    cus.set_address(address)
                    cus.set_state(state)
                    
                    
                    return customers

                else: # only update address 
                    # get new address
                    address = input("What is " + cus_first + " " + cus_last + "\'s new address? ")
                    
                    #update
                    cus.set_address(address)
                    
                    return customers
            else:
                
                print("Invalid option picked!!!")

    # if last name not found
    if not found:
        
        print()
        print(lastName + " does not exit in list of customers!!")

    return customers

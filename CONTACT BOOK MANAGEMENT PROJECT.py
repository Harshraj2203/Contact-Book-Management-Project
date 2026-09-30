# Create an empty dictionary
contacts = {}

# Create Main Menu
while True:
    print("\n***WELCOME TO PYTHON CONTACT BOOK MANAGEMENT APP***")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = input("Please choose an option (1/2/3/4/5/6/7) : ")

    # Create a new contact
    if choice == '1':
        name = input("Enter the name you want the contact to be saved = ")
        if name in contacts:
            print(f'CONTACT NAME {name} ALREADY EXISTS!')
        else:
            age = input("Enter age = ")
            email = input("Enter email = ")
            mobile = input("Enter mobile number = ")
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print(f'CONTACT NAME {name} HAS BEEN SAVED SUCCESSFULLY!')

    # View a contact
    elif choice == '2':
        name = input("Enter Contact name to view = ")
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age:{age}, Mobile Number:{mobile}, Email:{email}')
        else:
            print("CONTACT NOT FOUND!")

    # Update an existing contact
    elif choice == '3':
        name = input("Enter Contact name that you want to update = ")
        if name in contacts:
           age = input("Enter updated age = ")
           email = input("Enter updated email = ")
           mobile = input("Enter updated mobile number = ")
           contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
           print(f'CONTACT NAME {name} HAS BEEN UPDATED SUCCESSFULLY!')
        else:
            print("CONTACT NOT FOUND!")

    # Delete a contact
    elif choice == '4':
        name = input("Enter contact name to delete = ")
        if name in contacts:
            del contacts[name]
            print(f'CONTACT NAME {name} HAS BEEN DELETED SUCCESSFULLY!')
        else:
            print(" CONTACT NOT FOUND!")

    # Search contacts by name
    elif choice == '5':
        search_name = input("Enter contact name to search = ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name:{name}, Age:{age}, Mobile Number:{mobile}, Email:{email}')
                found = True
        if not found:
            print("NO CONTACT FOUND WITH THAT NAME")

    # Count contacts
    elif choice == '6':
        print(f'Total contacts in your contact book : {len(contacts)}')

    # Exit the program
    elif choice == '7':
        print("GOOD BYEE...CLOSING THE PROGRAM")
        break

    else:
        print("INVALID INPUT")




contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    favorite = input("Is this a favorite contact? (y/n): ").lower() == 'y'
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": favorite
    })
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact['name']} - Phone: {contact['phone']}, Email: {contact['email']}, Favorite: {'Yes' if contact['favorite'] else 'No'}")

def edit_contact():
    view_contacts()
    index = int(input("Enter the number of the contact to edit: ")) - 1
    if 0 <= index < len(contacts):
        contact = contacts[index]
        contact['name'] = input("Enter new name (or press enter to keep current): ") or contact['name']
        contact['phone'] = input("Enter new phone (or press enter to keep current): ") or contact['phone']
        contact['email'] = input("Enter new email (or press enter to keep current): ") or contact['email']
        favorite = input("Is this a favorite contact? (y/n): ").lower()
        if favorite in ['y', 'n']:
            contact['favorite'] = favorite == 'y'
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

def toggle_favorite():
    view_contacts()
    index = int(input("Enter the number of the contact to toggle favorite status: ")) - 1
    if 0 <= index < len(contacts):
        contacts[index]['favorite'] = not contacts[index]['favorite']
        print("Favorite status toggled successfully!")
    else:
        print("Invalid contact number.")

def view_favorites():
    favorites = [contact for contact in contacts if contact['favorite']]
    if not favorites:
        print("No favorite contacts found.")
    else:
        for i, contact in enumerate(favorites):
            print(f"{i+1}. {contact['name']} - Phone: {contact['phone']}, Email: {contact['email']}")

def delete_contact():
    view_contacts()
    index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

def main():
    while True:
        print("\n--- Todo List Application ---")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Toggle favorite status")
        print("5. View favorite contacts")
        print("6. Delete a contact")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            toggle_favorite()
        elif choice == '5':
            view_favorites()
        elif choice == '6':
            delete_contact()
        elif choice == '7':
            print("Thank you for using the Todo List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

contacts = {}


def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    if name not in contacts:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact '{name}' added successfully.")
    else:
        print(f"Contact '{name}' already exists.")


def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print(
            f"Updating contact '{name}'. Leave fields blank to keep existing values.")
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")


def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")


def search_contact():
    name = input("Enter the name of the contact you want to search: ")
    if name in contacts:
        contact_info = contacts[name]
        print(
            f"Contact '{name}': Phone: {contact_info['phone']}, Email: {contact_info['email']}")
    else:
        print(f"Contact '{name}' not found.")


def list_contacts():
    if contacts:
        print("Contacts:")
        for name in contacts:
            print(
                f"{name}: Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("No contacts found.")


while True:
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. List Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        update_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        list_contacts()
    elif choice == '6':
        print("Exiting Contact Manager.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")

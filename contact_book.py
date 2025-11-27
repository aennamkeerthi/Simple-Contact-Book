# Simple In-Memory Contact Book

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added!\n")

def view_contacts():
    if not contacts:
        print("No contacts yet.\n")
        return
    print("---- Contact List ----")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()

def search_contact():
    term = input("Search by name: ").lower()
    results = [c for c in contacts if term in c["name"].lower()]
    if results:
        print("---- Search Results ----")
        for c in results:
            print(f"{c['name']} - {c['phone']}")
    else:
        print("No matching contacts found.")
    print()

def edit_contact():
    view_contacts()
    if not contacts:
        return
    try:
        choice = int(input("Enter contact number to edit: ")) - 1
        if not (0 <= choice < len(contacts)):
            print("Invalid number!\n")
            return
    except ValueError:
        print("Invalid input.\n")
        return
    new_name = input("New name (leave blank to keep old): ")
    new_phone = input("New phone (leave blank to keep old): ")
    if new_name:
        contacts[choice]["name"] = new_name
    if new_phone:
        contacts[choice]["phone"] = new_phone
    print("Contact updated!\n")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    try:
        choice = int(input("Enter contact number to delete: ")) - 1
        if not (0 <= choice < len(contacts)):
            print("Invalid number!\n")
            return
    except ValueError:
        print("Invalid input.\n")
        return
    contacts.pop(choice)
    print("Contact deleted!\n")

def main():
    while True:
        print("---- Contact Book ----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        print()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

main()

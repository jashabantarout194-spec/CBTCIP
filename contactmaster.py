# ContactMaster - Simple Contact Management System

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    
    contacts[name] = {"phone": phone, "email": email}
    print("✅ Contact added successfully!\n")

def delete_contact():
    name = input("Enter name to delete: ")
    
    if name in contacts:
        del contacts[name]
        print("🗑️ Contact deleted!\n")
    else:
        print("❌ Contact not found!\n")

def search_contact():
    name = input("Enter name to search: ")
    
    if name in contacts:
        print(f"📞 Phone: {contacts[name]['phone']}")
        print(f"📧 Email: {contacts[name]['email']}\n")
    else:
        print("❌ Contact not found!\n")

def show_contacts():
    if not contacts:
        print("📭 No contacts available.\n")
    else:
        print("\n📒 Contact List:")
        for name, info in contacts.items():
            print(f"{name} - {info['phone']} - {info['email']}")
        print()

def menu():
    while True:
        print("===== CONTACTMASTER =====")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Show All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            delete_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            show_contacts()
        elif choice == "5":
            print("👋 Exiting ContactMaster")
            break
        else:
            print("❌ Invalid choice!\n")

# Run the program
menu()
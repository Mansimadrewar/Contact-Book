import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a contact
def add_contact(name, phone):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"✅ Contact added: {name} - {phone}")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 No contacts found.")
    else:
        print("📒 Your Contacts:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

# Search contact
def search_contact(name):
    contacts = load_contacts()
    found = [c for c in contacts if name.lower() in c["name"].lower()]
    if found:
        print("🔍 Search Results:")
        for c in found:
            print(f"{c['name']} - {c['phone']}")
    else:
        print("❌ No contact found with that name.")

# Delete contact
def delete_contact(name):
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    if len(new_contacts) < len(contacts):
        save_contacts(new_contacts)
        print(f"🗑️ Contact '{name}' deleted.")
    else:
        print("⚠️ No contact found with that name.")

# CLI Menu
def menu():
    while True:
        print("\n📘 Contact Book Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_contacts()
        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid option. Try again.")

if __name__ == "__main__":
    menu()

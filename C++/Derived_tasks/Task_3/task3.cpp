#include <iostream>
#include <map>
#include <string>

class AddressBook {
private:
    std::map<std::string, std::string> contacts;

public:
    void addContact(const std::string& name, const std::string& phone) {
        contacts[name] = phone;
        std::cout << "Contact added/updated successfully.\n";
    }

    void deleteContact(const std::string& name) {
        auto it = contacts.find(name);
        if (it != contacts.end()) {
            contacts.erase(it);
            std::cout << "Contact deleted successfully.\n";
        } else {
            std::cout << "Contact not found.\n";
        }
    }

    void deleteAllContacts() {
        contacts.clear();
        std::cout << "All contacts deleted successfully.\n";
    }

    void searchContact(const std::string& name) {
        auto it = contacts.find(name);
        if (it != contacts.end()) {
            std::cout << "Name: " << it->first << ", Phone: " << it->second << "\n";
        } else {
            std::cout << "Contact not found.\n";
        }
    }

    void listContacts() {
        if (contacts.empty()) {
            std::cout << "No contacts available.\n";
        } else {
            for (auto& contact : contacts) {
                std::cout << "Name: " << contact.first << ", Phone: " << contact.second << "\n";
            }
        }
    }

    void close() {
        std::cout << "Address book closed.\n";
    }
};

void displayMenu() {
    std::cout << "Address Book Menu:\n";
    std::cout << "1. Add/Update Contact\n";
    std::cout << "2. Delete Contact\n";
    std::cout << "3. Delete All Contacts\n";
    std::cout << "4. Search Contact\n";
    std::cout << "5. List All Contacts\n";
    std::cout << "6. Close Address Book\n";
    std::cout << "Choose an option: ";
}

int main() {
    AddressBook addressBook;
    int choice;
    std::string name, phone;

    do {
        displayMenu();
        std::cin >> choice;

        switch (choice) {
        case 1:
            std::cout << "Enter name: ";
            std::cin>>name;
            std::cout << "Enter phone: ";
            std::cin>>phone;
            addressBook.addContact(name, phone);
            break;
        case 2:
            std::cout << "Enter name to delete: ";
            std::getline(std::cin, name);
            addressBook.deleteContact(name);
            break;
        case 3:
            addressBook.deleteAllContacts();
            break;
        case 4:
            std::cout << "Enter name to search: ";
            std::getline(std::cin, name);
            addressBook.searchContact(name);
            break;
        case 5:
            addressBook.listContacts();
            break;
        case 6:
            addressBook.close();
            break;
        default:
            std::cout << "Invalid option. Please try again.\n";
        }
    } while (choice != 6);

    return 0;
}

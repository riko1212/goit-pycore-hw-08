import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __repr__(self):
        return f"Person({self.name}, {self.email}, {self.phone}, {self.favorite})"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, person: Person):
        self.contacts.append(person)

    def save_to_file(self, filename: str):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(filename: str):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return AddressBook()

    def __repr__(self):
        return f"AddressBook({self.contacts})"

def main():
    address_book = AddressBook.load_from_file("addressbook.pkl")


    address_book.add_contact(Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False))
    address_book.add_contact(Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False))


    address_book.save_to_file("addressbook.pkl")

    loaded_address_book = AddressBook.load_from_file("addressbook.pkl")
    print(loaded_address_book)

if __name__ == "__main__":
    main()

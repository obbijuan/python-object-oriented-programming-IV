from typing import List

"""
The Contact class is responsible for maintaining a global list of
all contacts ever  seen in a class variable, and for initializing
the name and address for an individual  contact:
"""

class Contact:

    all_contacts: List["Contact"] = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}"
            f")"
        )


c_1 = Contact("Dusty", "dusty@example.com")
c_2 = Contact("Steve", "steve@itmaybeahack.com")

contact_list = Contact.all_contacts
print(contact_list)

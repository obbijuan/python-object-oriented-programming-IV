from typing import List


"""
How do we apply inheritance in practice?:
The simplest and most obvious use of inheritance is to add
functionality to an existing class.
Let's start with a contact manager that tracks the names
and email addresses of several people.
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

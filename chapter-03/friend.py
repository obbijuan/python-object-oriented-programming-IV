from typing import List


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


"""
Inheritance : Overriding and super
"""
class Friend(Contact):

    def __init__(self, name: str, email: str, phone: str) -> None:
        super().__init__(name, email)
        self.phone = phone


f = Friend("Dusty", "Dusty@private.com", "555-1212")
print(Contact.all_contacts)
# [Friend('Dusty', 'Dusty@private.com')]

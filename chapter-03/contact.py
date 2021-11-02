from typing import List
from pprint import pprint

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



"""
Let's create a new Supplier class that acts like our
Contact class, but has an additional order method that
accepts a yet-to-be-defined Order object.
"""

class Supplier(Contact):

    def order(self, order: "Order") -> None:
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )



"""
Now, if we test this class, we see that all contacts,
including suppliers, accept a name and email address
in their __init__() method, but that only Supplier
instances have an order() method.
"""

c_1 = Contact("Dusty", "dusty@example.com")
c_2 = Contact("Steve", "steve@itmaybeahack.com")

# contact_list = Contact.all_contacts
# print(contact_list)

c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")

pprint(c.all_contacts)
# [Contact('Dusty', 'dusty@example.com'),
#  Contact('Steve', 'steve@itmaybeahack.com'),
#  Contact('Some Body', 'somebody@example.net'),
#  Supplier('Sup Plier', 'supplier@example.net')]

# c.order("I need pliers")
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# AttributeError: 'Contact' object has no attribute 'order'

s.order("I need pliers")
# If this were a real system we would send 'I need pliers' order to 'Sup Plier'

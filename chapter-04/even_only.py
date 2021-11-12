from typing import List

'''
We've provided a type hint suggesting we're creating a list of integer objects only.
To do this, we've overridden the append method to check two conditions that ensure 
the item is an even integer. We first check whether the input is an instance 
of the int type, and then use the modulo operator to ensure it is divisible by two.
If either of the two conditions is not met, the raise keyword causes an exception to occur.
'''


class EvenOnly(List[int]):

    def append(self, value: int) -> None:

        if not isinstance(value, int):
            raise TypeError("Only integers can be added")
        if value % 2 != 0:
            raise ValueError("Only even numbers can be added")
        super().append(value)


e = EvenOnly()
e.append("a string")
e.append(3)
e.append(2)

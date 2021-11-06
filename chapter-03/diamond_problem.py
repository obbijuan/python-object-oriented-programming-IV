
class BaseClass:
    num_base_calls = 0

    def call_me(self) -> None:
        print("Calling method on BaseClass")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self) -> None:
        BaseClass.call_me(self)
        print("Calling method on LeftSubclass")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self) -> None:
        BaseClass.call_me(self)
        print("Calling method on RightSubclass")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self) -> None:
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on Subclass")
        self.num_sub_calls += 1


s = Subclass()
s.call_me()

# Calling method on BaseClass
# Calling method on LeftSubclass
# Calling method on BaseClass
# Calling method on RightSubclass
# Calling method on Subclass



'''
Thus, we can see the base class's call_me() method being called twice. 
This could lead to some pernicious bugs if that method is doing 
actual work, such as depositing into a bank account, twice.
'''

print(f"{s.num_sub_calls} {s.num_left_calls} {s.num_right_calls} {s.num_base_calls}")
# 1 1 1 2
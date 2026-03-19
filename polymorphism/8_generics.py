from typing import Generic, TypeVar

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value


int_box = Box[int](0)      # ✅ IMPORTANT
str_box = Box[str]("hello")

print(int_box.get())        # 10
print(str_box.get())        # hello
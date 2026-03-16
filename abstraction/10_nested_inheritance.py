from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def method1(self):
        print("Method 1 implemented in A")


class B(A):
    @abstractmethod
    def method2(self):
        print("Method 2 implemented in B")
        return "Method 2 implemented in B"

    def method1(self):
        print("Method 1 implemented in B")


class C(B):
    def method1(self):
        print("Method 1 implemented in C")

    def method2(self):
        print("Method 2 implemented in C")


obj = C()
obj.method1()
obj.method2()

obj2 = B()
obj2.method1()
print(obj2.method2())


# Traceback (most recent call last):
""" File "/Users/shiveshsinghrao/Documents/Learnings/python_oops/abstraction/10_nested_inheritance.py", line 32, in <module>
    obj2 = B()
           ^^^
TypeError: Can't instantiate abstract class B with abstract method method2
"""

"""
so basically I cant directly create the obj of that class
 but create a new class then implement the abstract method and then use the subclass
"""

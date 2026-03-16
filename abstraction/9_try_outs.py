from abc import ABC, abstractmethod


class A:
    @abstractmethod
    def method1(self):
        print("Method 1")


class B(ABC, A):
    @abstractmethod
    def method2(self):
        print("Method 2")


class C(B):
    # def method1(self):
    #     print("Method 1 implemented in C")

    def method2(self):
        print("Method 2 implemented in C")


obj = C()
obj.method1()
obj.method2()

# A is a normal class with an abstract method method1.
#  B is an abstract class that inherits from A and has its own abstract method method2.
#  C is a concrete class that inherits from B and implements method2,
#  but it does not implement method1. When we create an instance of C and call method1,
#  it will print "Method 1" because it is inherited from A, and when we call method2,
#  it will print "Method 2 implemented in C" because it is implemented in C.

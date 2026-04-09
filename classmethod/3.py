# file: basic_classmethod.py

class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


def main():
    s1 = Student("Ravi")
    s2 = Student("Amit")

    print("Before change:")
    print(Student.school_name)
    print(s1.school_name)
    print(s2.school_name)

    Student.change_school("XYZ School")

    print("\nAfter change:")
    print(Student.school_name)
    print(s1.school_name)
    print(s2.school_name)


if __name__ == "__main__":
    main()
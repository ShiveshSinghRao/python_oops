"""
proving objects are not copy of a class
"""

class Car:
    wheels = 4

A = Car()
print(A.wheels)  # Output: 4 (Looks at Car.wheels, because A doesn't have its own yet)

Car.wheels = 6
print(A.wheels)  # Output: 6 (Still looks at Car.wheels, which changed to 6)

# THIS IS THE TURNING POINT:
A.wheels = "yo yo"  # Python creates a brand new, private attribute *only* on object A.

print(Car.wheels)  # Output: 6 (The class was NEVER touched!)
print(A.wheels)    # Output: "yo yo" (A is now looking at its own private variable instead of the class)

"""
The "Bulletin Board" Analogy:
The Class (Car) is like a shared bulletin board for all cars. 
It has a sticky note that says wheels = 6.

The Object (A) starts off empty-handed. 
When you ask A.wheels, A says, "I don't have a note, 
let me look at the shared bulletin board." It sees 6.

When you write A.wheels = "yo yo", you walk up to object A and
 stick a brand-new sticky note directly onto A's forehead.

Now, whenever you ask A for wheels,
 it looks at the note on its own forehead ("yo yo") and
   stops looking at the shared bulletin board.

Meanwhile, the shared bulletin board (Car.wheels) is still safely sitting at 6. 
If you create a second car object (e.g., B = Car()),
B.wheels will still be 6 because
A's changes didn't affect the class or other objects!
"""
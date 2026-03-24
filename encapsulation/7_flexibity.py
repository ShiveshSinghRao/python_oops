
""""
Imagine you built a library for a weather station. Initially, you store temperature in Celsius.

Phase 1: The Simple Way (No Encapsulation)
You give this code to 100 other developers:

Python
````
        class Sensor:
            def __init__(self, temp):
                self.temperature = temp # Public attribute

        # Other people use it like this:
        s = Sensor(25)
        print(s.temperature)
```` 
Phase 2: The Change
Suddenly, your boss says: "We're moving to the US. We must store everything in Fahrenheit internally, but our existing 100 developers still expect to read/write Celsius."

Without @property: You'd have to tell those 100 developers to change s.temperature to s.get_celsius(). Their code breaks.

With @property: You keep the interface the same.

2. The Flexible Way (Code Example)
We change the internal storage to _fahrenheit, but we keep the attribute name temperature for the outside world.
    """

class Sensor:
    def __init__(self, celsius_input):
        # We use the setter even in init to convert to Fahrenheit
        self.temperature = celsius_input 

    @property
    def temperature(self):
        """The 'External Interface' - still looks like Celsius"""
        # Formula: (F - 32) * 5/9
        return (self._fahrenheit - 32) * 5/9

    @temperature.setter
    def temperature(self, celsius):
        """The 'Internal Logic' - converts and stores as Fahrenheit"""
        print(f"Internal Log: Converting {celsius}°C to Fahrenheit")
        self._fahrenheit = (celsius * 9/5) + 32

# --- The "Flexibility" Proof ---
# The user's code DOES NOT CHANGE:
s = Sensor(25) 
print(s.temperature) # Output: 25.0

# But look under the hood:
print(s.__dict__)    # Output: {'_fahrenheit': 77.0}
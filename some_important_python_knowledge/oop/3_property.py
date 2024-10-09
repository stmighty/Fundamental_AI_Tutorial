class CelsiusWithoutProperty:
    def __init__(self, temperature=0):
        self.temperature = temperature

    # Explicit getter
    def get_temperature(self):
        return self.temperature

    # Explicit setter
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self.temperature = value


class CelsiusWithProperty:
    def __init__(self, temperature_var=0):
        self._temperature_attr = temperature_var

    @property
    def temperature(self):
        return self._temperature_attr

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature_attr = value




# Example without @property
c1 = CelsiusWithoutProperty(25)
print(c1.get_temperature())  # Accessing the value via getter method
c1.set_temperature(30)       # Setting the value via setter method
print(c1.get_temperature())  # Accessing the value again



# Example with @property
c2 = CelsiusWithProperty(25)
print(c2.temperature)  # Accessing the value like an attribute (no getter method)
c2.temperature = 30    # Setting the value like an attribute (no setter method)
print(c2.temperature)  # Accessing the value again

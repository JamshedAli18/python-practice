class Temperature:

    def __init__(self):
        self.c = 0.0
        self.f = 0.0
        self.k = 0.0
        self.r = 0.0
        self.menu()

    def menu(self):
        print("""
Choose an option:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Celsius to Rankine
6. Rankine to Celsius
Any other key to Exit
""")
        choice = input("→ ")

        if choice == '1':
            self.celsius_to_fahrenheit()
        elif choice == '2':
            self.fahrenheit_to_celsius()
        elif choice == '3':
            self.celsius_to_kelvin()
        elif choice == '4':
            self.kelvin_to_celsius()
        elif choice == '5':
            self.celsius_to_rankine()
        elif choice == '6':
            self.rankine_to_celsius()
        else:
            print("Exiting...")
            exit()

    def celsius_to_fahrenheit(self):
        self.c = float(input("Enter temperature in Celsius: "))
        self.f = (self.c * 9/5) + 32
        print(f"{self.c}°C = {self.f:.2f}°F")

    def fahrenheit_to_celsius(self):
        self.f = float(input("Enter temperature in Fahrenheit: "))
        self.c = (self.f - 32) * 5/9
        print(f"{self.f}°F = {self.c:.2f}°C")

    def celsius_to_kelvin(self):
        self.c = float(input("Enter temperature in Celsius: "))
        self.k = self.c + 273.15
        print(f"{self.c}°C = {self.k:.2f}K")

    def kelvin_to_celsius(self):
        self.k = float(input("Enter temperature in Kelvin: "))
        self.c = self.k - 273.15
        print(f"{self.k}K = {self.c:.2f}°C")

    def celsius_to_rankine(self):
        self.c = float(input("Enter temperature in Celsius: "))
        self.r = (self.c + 273.15) * 9/5
        print(f"{self.c}°C = {self.r:.2f}°R")

    def rankine_to_celsius(self):
        self.r = float(input("Enter temperature in Rankine: "))
        self.c = (self.r - 491.67) * 5/9
        print(f"{self.r}°R = {self.c:.2f}°C")



temp_converter = Temperature()


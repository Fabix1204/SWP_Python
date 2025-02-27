# Innner Functions
def generate_power(exponent, text):
    def power(base):
        print(text + str(base ** exponent))
        return base ** exponent
    return power

def generate_power_different(exponent):
    def power(base, text):
        print(text + str(base ** exponent))
        return base ** exponent
    return power

power2 = generate_power(2, "Berechnung: ")(3)
power3 = generate_power(3, "Berechnung: ")(3)

# args and kwargs
def person_address(name, street, city, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Straße: {street}")
    print(f"Stadt: {city}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
    
person = {
    "name": "Max Mustermann",
    "street": "Musterstraße 1",
    "city": "Musterstadt",
    "phone": "0123456789",
    "email": "max@mustermann.com"
    }

person_address(**person)

person_address("Fabian Leitner", "Musterstraße 2", *("Musterstadt", "Musterland"))
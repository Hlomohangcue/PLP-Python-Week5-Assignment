# Week 5 Python OOP Assignment
# Assignment 1: Design Your Own Class & Activity 2: Polymorphism Challenge

# =============================================================================
# ASSIGNMENT 1: SUPERHERO CLASS WITH INHERITANCE
# =============================================================================

class Superhero:
    """Base class for all superheroes"""
    
    # Class variable (shared by all instances)
    hero_count = 0
    
    def __init__(self, name, real_name, power_level=50, city="Unknown"):
        """Constructor to initialize superhero attributes"""
        # Instance attributes (unique to each object)
        self.name = name
        self.real_name = real_name
        self.power_level = power_level
        self.city = city
        self.energy = 100
        self.is_active = True
        
        # Increment class variable
        Superhero.hero_count += 1
    
    def introduce(self):
        """Method to introduce the superhero"""
        return f"I am {self.name}, protector of {self.city}!"
    
    def use_power(self, power_name="generic power"):
        """Method to use superhero powers"""
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.name} uses {power_name}! Energy: {self.energy}"
        else:
            return f"{self.name} is too tired to use powers!"
    
    def rest(self):
        """Method to restore energy"""
        self.energy = min(100, self.energy + 30)
        return f"{self.name} rests and recovers energy. Current energy: {self.energy}"
    
    def get_info(self):
        """Method to display hero information"""
        status = "Active" if self.is_active else "Retired"
        return f"""
Superhero Info:
- Name: {self.name}
- Real Name: {self.real_name}
- Power Level: {self.power_level}
- City: {self.city}
- Energy: {self.energy}
- Status: {status}
        """
    
    # Magic method for string representation
    def __str__(self):
        return f"{self.name} (Power Level: {self.power_level})"


class FlyingHero(Superhero):
    """Inherited class for heroes who can fly"""
    
    def __init__(self, name, real_name, power_level=50, city="Unknown", max_altitude=1000):
        # Call parent constructor
        super().__init__(name, real_name, power_level, city)
        # Add specific attribute for flying heroes
        self.max_altitude = max_altitude
        self.current_altitude = 0
    
    def fly(self, altitude=500):
        """Method specific to flying heroes"""
        if altitude > self.max_altitude:
            return f"{self.name} cannot fly above {self.max_altitude} feet!"
        
        self.current_altitude = altitude
        self.energy -= 10
        return f"{self.name} soars to {altitude} feet! Energy: {self.energy}"
    
    def land(self):
        """Method to land the flying hero"""
        if self.current_altitude > 0:
            self.current_altitude = 0
            return f"{self.name} lands safely on the ground."
        else:
            return f"{self.name} is already on the ground."
    
    # Override parent method (Polymorphism example)
    def use_power(self, power_name="flight-enhanced power"):
        if self.current_altitude > 0:
            power_name += f" from {self.current_altitude} feet high"
        return super().use_power(power_name)


class TechHero(Superhero):
    """Inherited class for technology-based heroes"""
    
    def __init__(self, name, real_name, power_level=50, city="Unknown", gadget_count=5):
        super().__init__(name, real_name, power_level, city)
        self.gadget_count = gadget_count
        self.suit_power = 100
    
    def use_gadget(self, gadget_name="high-tech device"):
        """Method specific to tech heroes"""
        if self.gadget_count > 0 and self.suit_power >= 15:
            self.gadget_count -= 1
            self.suit_power -= 15
            return f"{self.name} deploys {gadget_name}! Gadgets left: {self.gadget_count}, Suit power: {self.suit_power}"
        else:
            return f"{self.name} is out of gadgets or suit power is too low!"
    
    def recharge_suit(self):
        """Method to recharge the tech suit"""
        self.suit_power = 100
        return f"{self.name}'s suit is fully recharged!"
    
    # Override parent method (Polymorphism example)
    def use_power(self, power_name="tech-enhanced ability"):
        if self.suit_power >= 25:
            self.suit_power -= 10
            power_name += f" (Suit Power: {self.suit_power})"
        return super().use_power(power_name)


# =============================================================================
# ACTIVITY 2: POLYMORPHISM CHALLENGE - VEHICLES
# =============================================================================

class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, name, speed=0):
        self.name = name
        self.speed = speed
    
    def move(self):
        """Base move method - to be overridden by subclasses"""
        return f"{self.name} is moving at {self.speed} mph"
    
    def stop(self):
        """Common method for all vehicles"""
        return f"{self.name} has stopped"
    
    def __str__(self):
        return f"{self.name} (Speed: {self.speed} mph)"


class Car(Vehicle):
    """Car class with specific move behavior"""
    
    def __init__(self, name, speed=60, fuel_type="gasoline"):
        super().__init__(name, speed)
        self.fuel_type = fuel_type
    
    def move(self):
        """Polymorphic method - Car's version of move"""
        return f"🚗 {self.name} is driving on the road at {self.speed} mph"
    
    def honk(self):
        return f"{self.name} goes BEEP BEEP! 📯"


class Plane(Vehicle):
    """Plane class with specific move behavior"""
    
    def __init__(self, name, speed=500, altitude=30000):
        super().__init__(name, speed)
        self.altitude = altitude
    
    def move(self):
        """Polymorphic method - Plane's version of move"""
        return f"✈️ {self.name} is flying through the sky at {self.speed} mph at {self.altitude} feet"
    
    def takeoff(self):
        return f"{self.name} is taking off! 🛫"


class Boat(Vehicle):
    """Boat class with specific move behavior"""
    
    def __init__(self, name, speed=25, water_type="ocean"):
        super().__init__(name, speed)
        self.water_type = water_type
    
    def move(self):
        """Polymorphic method - Boat's version of move"""
        return f"⛵ {self.name} is sailing across the {self.water_type} at {self.speed} mph"
    
    def anchor(self):
        return f"{self.name} drops anchor! ⚓"


class Bicycle(Vehicle):
    """Bicycle class with specific move behavior"""
    
    def __init__(self, name, speed=15, gear=1):
        super().__init__(name, speed)
        self.gear = gear
    
    def move(self):
        """Polymorphic method - Bicycle's version of move"""
        return f"🚲 {self.name} is pedaling in gear {self.gear} at {self.speed} mph"
    
    def ring_bell(self):
        return f"{self.name} rings the bell! 🔔"


# =============================================================================
# DEMONSTRATION CODE
# =============================================================================

def demonstrate_superheroes():
    """Function to demonstrate superhero classes"""
    print("=" * 60)
    print("ASSIGNMENT 1: SUPERHERO CLASS DEMONSTRATION")
    print("=" * 60)
    
    # Create different types of superheroes
    hero1 = Superhero("Captain Shield", "Steve Rogers", 85, "New York")
    hero2 = FlyingHero("Sky Guardian", "Diana Prince", 90, "Metropolis", 5000)
    hero3 = TechHero("Iron Defender", "Tony Stark", 95, "Los Angeles", 10)
    
    heroes = [hero1, hero2, hero3]
    
    # Demonstrate each hero
    for hero in heroes:
        print(f"\n{hero.introduce()}")
        print(hero.get_info())
        
        # Use their powers
        print(hero.use_power())
        
        # Demonstrate specific abilities
        if isinstance(hero, FlyingHero):
            print(hero.fly(3000))
            print(hero.use_power("Aerial Strike"))
            print(hero.land())
        elif isinstance(hero, TechHero):
            print(hero.use_gadget("Repulsor Ray"))
            print(hero.recharge_suit())
        
        print(hero.rest())
        print("-" * 40)
    
    print(f"\nTotal heroes created: {Superhero.hero_count}")


def demonstrate_polymorphism():
    """Function to demonstrate polymorphism with vehicles"""
    print("\n" + "=" * 60)
    print("ACTIVITY 2: POLYMORPHISM CHALLENGE DEMONSTRATION")
    print("=" * 60)
    
    # Create different vehicles
    vehicles = [
        Car("Tesla Model 3", 120, "electric"),
        Plane("Boeing 747", 550, 35000),
        Boat("Sailboat Adventure", 30, "Mediterranean Sea"),
        Bicycle("Mountain Bike", 20, 5)
    ]
    
    # Demonstrate polymorphism - same method name, different behaviors
    print("\n🎭 POLYMORPHISM IN ACTION - Different vehicles, same move() method:")
    print("-" * 70)
    
    for vehicle in vehicles:
        print(vehicle.move())  # Each class implements move() differently!
        
        # Demonstrate specific methods
        if isinstance(vehicle, Car):
            print(vehicle.honk())
        elif isinstance(vehicle, Plane):
            print(vehicle.takeoff())
        elif isinstance(vehicle, Boat):
            print(vehicle.anchor())
        elif isinstance(vehicle, Bicycle):
            print(vehicle.ring_bell())
        
        print(vehicle.stop())
        print()


def demonstrate_oop_concepts():
    """Function to demonstrate key OOP concepts"""
    print("=" * 60)
    print("KEY OOP CONCEPTS DEMONSTRATED:")
    print("=" * 60)
    
    concepts = [
        "🏗️ CLASSES & OBJECTS: Created Superhero and Vehicle classes with multiple instances",
        "🔧 CONSTRUCTORS: Used __init__() to initialize objects with unique values",
        "🧬 INHERITANCE: FlyingHero and TechHero inherit from Superhero",
        "🎭 POLYMORPHISM: Same method name (move()) behaves differently in each vehicle class",
        "🔒 ENCAPSULATION: Used private-like attributes and public methods",
        "📊 CLASS vs INSTANCE VARIABLES: hero_count (class) vs name, power_level (instance)",
        "🔄 METHOD OVERRIDING: Subclasses override parent methods with super()",
        "✨ MAGIC METHODS: __str__() for string representation"
    ]
    
    for concept in concepts:
        print(f"  {concept}")
    print()


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🦸‍♂️ WEEK 5 PYTHON OOP ASSIGNMENT 🦸‍♀️")
    print("Created by: Hlomohang Sethuntsa")
    
    # Run demonstrations
    demonstrate_oop_concepts()
    demonstrate_superheroes()
    demonstrate_polymorphism()
    
    print("\n" + "=" * 60)
    print("🎉 ASSIGNMENT COMPLETE! All OOP concepts demonstrated successfully!")
    print("=" * 60)
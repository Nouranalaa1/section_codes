class Memento:
	def __init__(self, file, content):
		
		self.file = file     
		self.content = content

class X:
	def __init__(self, file_path):

		self.file = file_path
		self.content = ""


	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class Y:

	def save(self, x):
		self.mem = x.save()

	def undo(self, x):
		x.undo(self.mem)


if __name__ == '__main__':
	y = Y()

	x = X("GFG.txt")   #file = object , content = ""

	x.write("First vision of Data\n")   #file = object , content = "First vision of Data \n"
	print(x.content + "\n\n")

	y.save(x) # Memento file = object , content = "First vision of Data \n"

	x.write("Second vision of Data\n")  #file = object , content = "First vision of Data \n Second vision of Data"

	print(x.content + "\n\n")

	y.undo(x)

	print(x.content + "\n\n")  #file = object , content = "First vision of Data "
###################################################################################
class GameState:
    def __init__(self, level, health):
        self.level = level
        self.health = health

class Game:
    def __init__(self):
        self._level = 1
        self._health = 100

    def play(self):
        # Simulating gameplay, level up, and health changes
        self._level += 1
        self._health -= 10
        print(f"Level: {self._level}, Health: {self._health}")

    def save_state(self):
        return GameState(self._level, self._health)

    def load_state(self, state):
        self._level = state.level
        self._health = state.health

# Usage
game = Game()

# Play and save state
game.play()
saved_state = game.save_state()

# Play again
game.play()

# Load saved state
game.load_state(saved_state)
print("After loading saved state:")
print(f"Level: {game._level}, Health: {game._health}")

"""
the factory design
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

# Usage
animal1 = AnimalFactory.create_animal("dog")
print(animal1.speak())  # Output: Woof!

animal2 = AnimalFactory.create_animal("cat")
print(animal2.speak())  # Output: Meow!

"""
The Builder Pattern
"""
class Computer:
    def __init__(self, case, motherboard, cpu, memory, storage, gpu=None):
        self.case = case
        self.motherboard = motherboard
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.gpu = gpu

    def display(self):
        print("Computer Configuration:")
        print(f"Case: {self.case}")
        print(f"Motherboard: {self.motherboard}")
        print(f"CPU: {self.cpu}")
        print(f"Memory: {self.memory}")
        print(f"Storage: {self.storage}")
        if self.gpu:
            print(f"GPU: {self.gpu}")


class ComputerBuilder:
    def __init__(self):
        self._computer = None

    def build_case(self, case):
        self.case = case
        return self

    def build_motherboard(self, motherboard):
        self.motherboard = motherboard
        return self

    def build_cpu(self, cpu):
        self.cpu = cpu
        return self

    def build_memory(self, memory):
        self.memory = memory
        return self

    def build_storage(self, storage):
        self.storage = storage
        return self

    def build_gpu(self, gpu):
        self.gpu = gpu
        return self

    def build(self):
        return Computer(self.case, self.motherboard, self.cpu, self.memory, self.storage, self.gpu)


# Usage
builder = ComputerBuilder()
computer = builder.build_case("ATX Mid Tower") \
    .build_motherboard("MSI B450 Tomahawk") \
    .build_cpu("AMD Ryzen 5 3600") \
    .build_memory("16GB DDR4 RAM") \
    .build_storage("1TB SSD") \
    .build_gpu("NVIDIA GeForce RTX 3060") \
    .build()

computer.display()


"""
   Singleton Method 
"""
import copy

class Singleton():
    "The Singleton Class"
    value = []

    def __new__(cls):
        return cls #override the classes __new__ method to return a reference to itself
        #return object.__new__(cls) #what would be the out? and why?

    # def __init__(self):
    #     print("in init")

    @staticmethod
    def static_method():
        

    @classmethod
    def class_method(cls):
        
        print(cls.value)

# The Client
# All uses of singleton point to the same memory address (id)
print(f"id(Singleton)\t= {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT3)\t= {id(OBJECT3)}")


"""
Facade is a type of Structural Design Patterns
"""
# Subsystem classes
class CPU:
    def freeze(self):
        print("CPU freezing...")

    def jump(self, position):
        print(f"CPU jumping to position {position}...")

    def execute(self):
        print("CPU executing...")

class Memory:
    def load(self, position, data):
        print(f"Memory loading data {data} at position {position}...")

class HardDrive:
    def read(self, lba, size):
        return f"Data from sector {lba} with size {size}"

# Facade class
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        data = self.hard_drive.read(0, 1024)
        self.memory.load(0, data)
        self.cpu.jump(0)
        self.cpu.execute()

# Client code
if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start()


"""
Flyweight is a type of Structural Design Patterns
"""

from abc import ABC,abstractmethod

class Flyweight(ABC):
    @abstractmethod
    def operation(self, extrinsic_state):
        pass
    
class ConcreteFlyweight(Flyweight):
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state
    def operation(self, extrinsic_state):
        print(self.intrinsic_state, extrinsic_state)

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}
    def get_fly(self,intrinsic_state):
        if intrinsic_state not in self.flyweights:
            self.flyweights[intrinsic_state] = ConcreteFlyweight(intrinsic_state)
        return self.flyweights[intrinsic_state]  
class Client:
    def __init__(self,factory):
        self.factory = factory
    def operation(self, extrinsic_state):
	     print(self.intrinsic_state, extrinsic_state)

class Client:
    def __init__(self, factory):
        self.factory = factory

    def operation(self, extrinsic_state1, extrinsic_state2):
        fly1 = self.factory.get_fly(1)
        fly2 = self.factory.get_fly(2)

        fly1.operation(extrinsic_state1)
        fly2.operation(extrinsic_state2)
    
factory = FlyweightFactory()
client = Client(factory)
client.operation(10, 20)
#################################
from abc import ABC, abstractmethod

# Flyweight interface
class Shape(ABC):
    @abstractmethod
    def draw(self, x, y):
        pass

# ConcreteFlyweight implementation
class Circle(Shape):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        print(f"Drawing a circle with color {self.color} at ({self.x}, {self.y}) with radius {self.radius}")

# FlyweightFactory
class ShapeFactory:
    def __init__(self):
        self.shapes = {}

    def get_shape(self, color):
        if color not in self.shapes:
            self.shapes[color] = []
        if not self.shapes[color]:
            self.shapes[color].append(Circle(0, 0, 0, color))
        return self.shapes[color][-1]

# Client
class Client:
    def __init__(self, factory):
        self.factory = factory

    def draw_shapes(self, shapes_data):
        for data in shapes_data:
            shape = self.factory.get_shape(data["color"])
            shape.x = data["x"]
            shape.y = data["y"]
            shape.radius = data["radius"]
            shape.draw()

# Usage
factory = ShapeFactory()
client = Client(factory)
shapes_data = [
    {"color": "red", "x": 10, "y": 10, "radius": 5},
    {"color": "green", "x": 20, "y": 20, "radius": 10},
    {"color": "red", "x": 30, "y": 30, "radius": 15},
]
client.draw_shapes(shapes_data)


"""
Adapter
"""
# Existing class with a specific interface
class EuropeanSocket:
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

# Target interface expected by the client
class USASocketInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def ground(self):
        pass

# Adapter class that adapts the EuropeanSocket to the USASocketInterface
class EuropeanToUSAAdapter(USASocketInterface):
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def voltage(self):
        # Convert voltage from 230V to 120V
        return 120

    def live(self):
        return self.european_socket.live()

    def neutral(self):
        return self.european_socket.neutral()

    def ground(self):
        # European sockets do not have a ground, so return 0
        return 0

# Client code
def connect_device_to_usa_socket(socket):
    print("Voltage:", socket.voltage())
    print("Live:", socket.live())
    print("Neutral:", socket.neutral())
    print("Ground:", socket.ground())

if __name__ == "__main__":
    european_socket = EuropeanSocket()
    adapter = EuropeanToUSAAdapter(european_socket)
    connect_device_to_usa_socket(adapter)

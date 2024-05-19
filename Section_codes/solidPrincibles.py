"""
Single Responsibility Principle
The Single Responsibility Principle (SRP) is one of the five SOLID principles of object-oriented design. 
It states that a class should have only one reason to change, meaning it should have only one responsibility or job.
This principle helps in making the system more modular, easier to understand, and maintain.
"""
#Problem//////////////////////////////////////////
class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def print_book(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Content: {self.content}')

    def save_to_database(self):
        # Code to save the book to the database
        pass

# Usage
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Some content...")
book.print_book()
book.save_to_database()

#Solve//////////////////////////////////////////
class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

class BookPrinter:
    @staticmethod
    def print_book(book):
        print(f'Title: {book.title}')
        print(f'Author: {book.author}')
        print(f'Content: {book.content}')

class BookRepository:
    @staticmethod
    def save_to_database(book):
        # Code to save the book to the database
        pass

# Usage
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Some content...")
BookPrinter.print_book(book)
BookRepository.save_to_database(book)

"""
Open-Closed Principle
The Open-Closed Principle (OCP) is another important principle in object-oriented design,
stating that software entities (such as classes, modules, and functions) should be open for extension but closed for modification. 
This means you should be able to add new functionality to a system without changing the existing code.
"""

#Problem//////////////////////////////////////////
class PaymentProcessor:
    def process_payment(self, payment_type):
        if payment_type == "credit_card":
            self.process_credit_card()
        elif payment_type == "paypal":
            self.process_paypal()
        # More payment types...
    
    def process_credit_card(self):
        # Process credit card payment
        pass
    
    def process_paypal(self):
        # Process PayPal payment
        pass

# Usage
processor = PaymentProcessor()
processor.process_payment("credit_card")


#Solve//////////////////////////////////////////
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self):
        pass

class CreditCardPayment(Payment):
    def process(self):
        # Process credit card payment
        pass

class PaypalPayment(Payment):
    def process(self):
        # Process PayPal payment
        pass

class PaymentProcessor:
    def process_payment(self, payment: Payment):
        payment.process()

# Usage
processor = PaymentProcessor()
credit_card_payment = CreditCardPayment()
paypal_payment = PaypalPayment()

processor.process_payment(credit_card_payment)
processor.process_payment(paypal_payment)

"""
Liskov Substitution Principle
The Liskov Substitution Principle (LSP) is another key principle in object-oriented design. 
It states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. 
Essentially, subclasses should behave in a way that won't cause unexpected results when used in place of their superclass.
"""
#Problem//////////////////////////////////////////
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # Ensure width and height are the same
    
    def set_height(self, height):
        self.width = height
        self.height = height  # Ensure width and height are the same

# Usage
def print_area(rectangle: Rectangle):
    rectangle.set_width(5)
    rectangle.set_height(10)
    print(f'Area: {rectangle.get_area()}')

rect = Rectangle(2, 3)
print_area(rect)  # Output: Area: 50

sq = Square(2, 2)
print_area(sq)    # Output: Area: 100 (incorrect for a square)


#Solve//////////////////////////////////////////
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def set_side(self, side):
        self.side = side
    
    def get_area(self):
        return self.side * self.side

# Usage
def print_area(shape: Shape):
    print(f'Area: {shape.get_area()}')

rect = Rectangle(5, 10)
print_area(rect)  # Output: Area: 50

sq = Square(10)
print_area(sq)    # Output: Area: 100

"""
Interface Segregation Principle
The Interface Segregation Principle (ISP) is one of the SOLID principles of object-oriented design. 
It states that no client should be forced to depend on methods it does not use. 
In other words, larger interfaces should be split into smaller, 
more specific ones so that clients only need to know about the methods that are of interest to them.
"""
#Problem//////////////////////////////////////////
class MultiFunctionPrinter:
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document):
        pass

class OldFashionedPrinter(MultiFunctionPrinter):
    def print(self, document):
        # Print the document
        pass

    def scan(self, document):
        raise NotImplementedError("Scan not supported")

    def fax(self, document):
        raise NotImplementedError("Fax not supported")

# Usage
printer = OldFashionedPrinter()
printer.print("document")
printer.scan("document")  # Raises NotImplementedError


#Solve//////////////////////////////////////////
class Printer:
    def print(self, document):
        pass

class Scanner:
    def scan(self, document):
        pass

class FaxMachine:
    def fax(self, document):
        pass

class SimplePrinter(Printer):
    def print(self, document):
        # Print the document
        pass

class MultiFunctionDevice(Printer, Scanner, FaxMachine):
    def print(self, document):
        # Print the document
        pass

    def scan(self, document):
        # Scan the document
        pass

    def fax(self, document):
        # Fax the document
        pass

# Usage
printer = SimplePrinter()
printer.print("document")

mfd = MultiFunctionDevice()
mfd.print("document")
mfd.scan("document")
mfd.fax("document")

"""
The Dependency Inversion Principle (DIP) is the last of the SOLID principles. 
It states that high-level modules should not depend on low-level modules. 
Both should depend on abstractions. Additionally, abstractions should not depend on details; 
details should depend on abstractions. This principle helps in reducing the dependency between the high-level business logic and the low-level implementation details, 
promoting a more flexible and maintainable codebase.
"""
#Problem//////////////////////////////////////////
class EmailSender:
    def send(self, message):
        print(f"Sending email: {message}")

class SmsSender:
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self):
        self.email_sender = EmailSender()
        self.sms_sender = SmsSender()

    def send_notification(self, message, method):
        if method == "email":
            self.email_sender.send(message)
        elif method == "sms":
            self.sms_sender.send(message)

# Usage
service = NotificationService()
service.send_notification("Hello, World!", "email")
service.send_notification("Hello, World!", "sms")


#Solve//////////////////////////////////////////
from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(MessageSender):
    def send(self, message):
        print(f"Sending email: {message}")

class SmsSender(MessageSender):
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send_notification(self, message):
        self.sender.send(message)

# Usage
email_sender = EmailSender()
sms_sender = SmsSender()

email_service = NotificationService(email_sender)
sms_service = NotificationService(sms_sender)

email_service.send_notification("Hello, World!")  # Sending email: Hello, World!
sms_service.send_notification("Hello, World!")    # Sending SMS: Hello, World!


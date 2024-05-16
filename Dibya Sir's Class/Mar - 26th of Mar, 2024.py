import re

pattern = r'I study BTech in Kaziranga University'
pattern2 = re.sub('BTech', 'BCA', pattern)

print(pattern2)


# Extended regular expression

# It is only supported after the VERBOSE flag
# It is not supported natively

import re

pattern = re.compile(r'''
                     
                     \b # Word boundary
                     \d{3} # Match exactly three digits
                     
                     ''', re.VERBOSE)
                     
text = "Phone numbers: 123-45-6789, 987654321, 555-5555"

matches = pattern.findall(text)
print(matches)


# Wild card "."
# dot represents a single character that can be anything

import re

pattern = re.compile(r'gr.y')
text = "The gray cat jumped over the lazy dog"
matches = pattern.findall(text)
print(matches)

# Object oriented programming

# Class
# Object

# Characteristics of Object Oriented Programming

# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction


# In java, multi-level is supported but multiple is not supported
# Multiple parents with one child is not supported because it may 
# lead to security breach


class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
        
class Dog(Animal):
    def speak(self):
        return f'{self.name} says Woof!'

class Cat(Animal):
    def speak(self):
        return f'{self.name} says Meouw!'

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())



































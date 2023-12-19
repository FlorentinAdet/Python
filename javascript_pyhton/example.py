# example.py

def python_function(name = None, age = None):
    return "Hello from Python! " + name + " has " + str(age) + " years." 

def compter_majuscules(text = None):
    count = sum(1 for char in text if char.isupper())
    return str(count)
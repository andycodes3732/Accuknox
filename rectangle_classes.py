# Here is a simple implementation of a Rectangle class which meets the desired requirements:

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rectangle = Rectangle(10, 5)
for dimension in rectangle:
    print(dimension)

# Explanation:
# The Rectangle class is initialized with length and width.
# The __iter__ method is defined to make the class iterable. It uses yield to first return the length and then the width in the specified format.
# When we iterate over an instance of Rectangle, it will output the length and width as dictionaries.
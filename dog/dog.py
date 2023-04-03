"""This module creates a new class Dog and it inherits from Animal class."""
from typing import Final

from animals.animal import Animal


class Dog(Animal):
    """Dog is a class which inherits from Animal."""

    def __init__(self, species, breed: str):
        """
        The Dog constructor.

        :param breed: The breed
        """
        # Inherits constructor from animal class to define class attributes in same way
        super().__init__(species)
        self.breed: Final[str] = breed

    def __eq__(self, other):
        """
        Compares two Dog class species and breeds.

        :param other: a different Dog instance
        :return boolean (True or False)
        """
        return self.species == other.species and self.breed == other.breed

    def bark(self):
        """Docstring of dog barking."""
        print("WOOF")


def main():
    """Runs an instance of the Dog class."""
    scooby = Dog("Dog", "Great Danes")
    # Calls a Dog class method
    scooby.bark()


if __name__ == "__main__":
    main()

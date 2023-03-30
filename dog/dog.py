from typing import Final

class Dog:
    """Dog is a class which will inherit from Animal"""
    # It will inherit from Animal once a pull request has been approved into dev branch

    def __init__(self, species: str):
        """
        The Dog constructor.

        :param species: The species
        """
        self.species: Final[str] = species

    def bark(self):
        print("WOOF")

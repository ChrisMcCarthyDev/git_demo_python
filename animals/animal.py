from typing import Final


class Animal:
    """Animal is a base class for all animals."""

    def __init__(self, species: str):
        """
        The Animal constructor.

        :param species: The species.
        """
        self.species: Final[str] = species

    def __str__(self):
        return f"I'm a {self.species}!"

    def __repr__(self):
        return f"{self.__class__.__name__}(species={self.species})"

    def __iter__(self):
        yield "species", self.species

    def __hash__(self):
        return hash(self.species)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return hash(self) == hash(other)
        return False

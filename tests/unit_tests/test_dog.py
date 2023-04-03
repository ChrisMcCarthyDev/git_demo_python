"""Python module to test Dog class."""
import pytest

from dog.dog import Dog


@pytest.mark.unit_test
def test_dog_eq():
    """Test if two different Dog classes are equal."""
    dog_1 = Dog("Dog", "French Bulldog")
    dog_2 = Dog("Dog", "French Bulldog")

    assert dog_1 == dog_2
    assert dog_1 == dog_1


@pytest.mark.unit_test
def test_animal_not_eq():
    """Test the Dog eq function with different Dog classes."""
    dog_1 = Dog("Dog", "French Bulldog")
    dog_2 = Dog("Dog", "Rottweiler")

    assert dog_1 != dog_2

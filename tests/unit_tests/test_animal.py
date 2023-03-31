import pytest

from animals.animal import Animal


@pytest.mark.unit_test
def test_animal_eq():
    """Test the Animal eq function with matching instances"""
    animal_1 = Animal("Fish")
    animal_2 = Animal("Fish")

    assert animal_1 == animal_1
    assert animal_1 == animal_2


@pytest.mark.unit_test
def test_animal_not_eq():
    """Test the Animal eq function with non-matching instances."""
    animal_1 = Animal("Fish")
    animal_2 = Animal("fish")

    assert animal_1 != animal_2

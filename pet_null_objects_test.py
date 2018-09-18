from unittest import TestCase

from pet_null_objects_example import Human, Dog


class PetNullObjectsTest(TestCase):
    def test_owner_should_act_on_pet(self):
        pet = Dog()
        owner = Human()
        owner.express_affection_towards(pet)

        assert pet.isHappy

    def test_owner_should_act_on_null_pet(self):
        pet = None
        owner = Human()
        owner.express_affection_towards(pet)

        #assert pet.isHappy
        # uncomment this line too ^^

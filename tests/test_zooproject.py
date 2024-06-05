import unittest
from unittest import TestCase
from src.zoopark import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):

    def setUp(self) -> None:
        self.zoo_1 = Zoo()
        self.zookeeper_1 = ZooKeeper()
        self.fence_1 = Fence()
        self.animal_1 = Animal()
        # Non obbligatorio, possiamo istanziare nelle funzioni test

    def test_animal_dimension(self):
        self.zookeeper_1.add_animal(self.animal_1, self.fence_1)
        result = len(self.fence_1.animals)
        message = f"Error: not animal in fence"
        self.assertEqual(result, 0, message) # Se result = 0 scrivi message

    def test_2(self):
        pass



if __name__ == "__main__":
    unittest.main()
        
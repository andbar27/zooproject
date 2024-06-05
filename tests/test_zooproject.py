import unittest
from unittest import TestCase
from src.zoopark import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):

    def setUp(self) -> None:
        self.zk = ZooKeeper("gino","paoli","gp001")
        pass
        self.zookeeper_1 = ZooKeeper("gino","paoli","gp001")
        self.fence_1 = Fence(area=0)
        self.animal_1 = Animal()
        self.zoo_1 = Zoo([self.fence_1],[self.zookeeper_1])
        # Non obbligatorio, possiamo istanziare nelle funzioni test

    def test_animal_dimension(self):
        fence_1 = Fence(0, 0, "Savana")
        animal_1 = Animal("pino", "Cane", 1, 1, 1, "Savana")
        zookeeper_1 = ZooKeeper("gino", "paoli", "gp001")
        zookeeper_1.add_animal(animal_1, fence_1)
        result = len(fence_1.animals)
        message = f"Error: area is 0 so the animal should not add in the fence"
        self.assertEqual(result, 0, message) # Se result = 0 scrivi message

    def test_animal_habitat(self):
        a2 = Animal("luna", "gatto", 7, 2, 2, "Casa")
        f2 = Fence(10, 10, "Savana")
        self.zk.add_animal(a2, f2)
        result = len(f2.animals)
        message = "Error: habitat is different, so the animal should not add in the fence"
        self.assertEqual(result, 0, message)
        
    def test_clean(self):
        a2 = Animal("luna", "gatto", 7, 2, 2, "Savana")
        f2 = Fence(10, 10, "Savana")
        self.zk.add_animal(a2, f2)
        result = self.zk.clean(f2)
        message = "Error: result of clean is not right, Expected 0.667"
        self.assertEqual(result, 0.667, message)

        a2 = Animal("luna", "gatto", 7, 2, 2, "Savana")
        f2 = Fence(4, 10, "Savana")
        self.zk.add_animal(a2, f2)
        result = self.zk.clean(f2)
        message = "Error: result of clean is not right, Expected: 4"
        self.assertEqual(result, 4, message)

    def test_feed(self):
        a1 = Animal("a1", "coniglio", 1, 2, 2, "gabbia")
        f1 = Fence(4, 1, "gabbia")
        self.zk.add_animal(a1, f1)
        self.zk.feed(a1)
        result = a1.height
        message = "Error: height must be already 2, because there isn't space in fence, Expected: 2"
        self.assertEqual(result, 2, message)

        a1 = Animal("a1", "coniglio", 1, 2, 2, "gabbia")
        f1 = Fence(5, 1, "gabbia")
        self.zk.add_animal(a1, f1)
        self.zk.feed(a1)
        result = a1.height
        message = "Error: height must be height + 2%, Expected: 2.04"
        self.assertEqual(result, 2*1.02, message)
    
    def test_remove(self):
        a1 = Animal("a1", "coniglio", 1, 2, 2, "gabbia")
        f1 = Fence(4, 1, "gabbia")
        a2 = Animal("a2", "uccello", 1, 1, 1, "gabbia")
        self.zk.add_animal(a1, f1)
        result = False
        try:
            self.zk.remove_animal(a2, f1)
        except Exception:
            result = True
        message = "Runtime error, try to remove animal not present"
        self.assertEqual(result, False, message)
    

if __name__ == "__main__":
    unittest.main()
        
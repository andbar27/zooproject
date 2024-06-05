class Animal:
    def __init__(self, name: str = "Animal", species: str = "Species", age: float = 1.0,
                 height: float = 1.0, width: float = 1.0,
                 preferred_habitat: str = "Habitat"):
        self.name = name
        self.species = species
        if(age <= 0): age = 1.0 
        self.age = age
        if(height < 0): height = 0.0
        self.height = height
        if(width < 0): width = 0.0
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / self.age), 3)
        self.fence = None

    def __str__(self) -> str:
        message = f"Animal(name={self.name}, species={self.species}, age={self.age}," \
        + f" height={self.height}, width={self.width}, habitat={self.preferred_habitat}," \
        + f" health={self.health})\n"
        return message

class Fence:
    def __init__(self, area: float = 1.0, temperature: float = 0.0, 
                 habitat: str = "Habitat",  animals: list[Animal] = []):
        if area < 0: area = 0.0
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
        if len(animals) > 0: self._addAnimals(animals)  #add animal only if the animal isn't in other fence

    def _addAnimal(self, animal: Animal):
        if self.habitat == animal.preferred_habitat and animal.fence == None:
            animalArea = animal.height * animal.width
            if self.area >= animalArea:
                self.area -= animalArea
                self.animals.append(animal)
                animal.fence = self

    def _addAnimals(self, animals: list[Animal]):
        for animal in animals:
            self._addAnimal(animal)
    
    def __str__(self) -> str:
        message = f"\nFence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})\n\nwith animals:\n\n"
        for animal in self.animals:
            message += f"{animal}\n"
        return message
    
    # def __str__(self) -> str:
    #     message = f"(area={self.area}, temperature={self.temperature}, habitat={self.habitat})\nwith animals:\n"
    #     for animal in self.animals:
    #         message += f"\t\t\t{animal}\n"
    #     return message


class ZooKeeper:
    def __init__(self, name: str = "Name", surname: str = "Surname", id: str = "Id"):
        self.name = name
        self.surname = surname
        self.id = id
    
    def add_animal(self, animal: Animal, fence: Fence):
        animalArea = animal.height * animal.width
        if animal.preferred_habitat == fence.habitat and animal not in fence.animals:
            if animalArea <= fence.area:
                fence.area -= animalArea
                fence.animals.append(animal)
                if animal.fence:    #if the animal is already in other fence, 
                                    #add animal in this fence and remove from the previous
                    self.remove_animal(animal, animal.fence)
                animal.fence = fence

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            animalArea = animal.height * animal.width
            fence.area += animalArea
            animal.fence = None

    def feed(self, animal: Animal):
        tempHeight = animal.height + (animal.height / 100 * 2)
        tempWidth = animal.width + (animal.width / 100 * 2)
        tempAnimalArea = tempHeight * tempWidth
        animalArea = animal.height * animal.width
        diffAnimalArea = tempAnimalArea - animalArea

        fence = animal.fence

        if diffAnimalArea <= fence.area:
            fence.area -= diffAnimalArea
            animal.height = tempHeight
            animal.width = tempWidth
            animal.health += (animal.health / 100)

    def clean(self, fence: Fence):
        totalAnimalArea = 0.0
        animals = fence.animals
        for animal in animals:
            areaAnimal = animal.height * animal.width
            totalAnimalArea += areaAnimal
        if fence.area == 0:
            return totalAnimalArea
        areaRatio = totalAnimalArea / fence.area
        return areaRatio

    def __str__(self) -> str:
        message = f"\nZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"
        return message



class Zoo:
    def __init__(self, fences: list[Fence] = [], 
                 zoo_keepers: list[ZooKeeper] = [],
                 name: str = "Zoo",):
        self.name = name
        self.fences = fences
        self.zookeepers = zoo_keepers
    
    def describe_zoo(self):
        sepFence = "#" * 30 + "\n"
        message = ""
        
        message += "Guardians:\n"
        for zookeeper in self.zookeepers:
            message += f"{zookeeper}\n"

        message += "\nFances:\n"
        for fence in self.fences:
            if len(fence.animals) == 0: #Print only fences with animals
                continue
            message += f"{fence}" + sepFence
        
        print(message)

    def __str__(self) -> str:   #for use this decomment str of animal
        sepFence = "#" * 30 + "\n"
        message = self.name
        
        message += "\n\tFances:\n"
        for fence in self.fences:
            if len(fence.animals) == 0: #Print only fences with animals
                continue
            message += f"\t\t{fence}\t\t" + sepFence
        
        message += "\n\tGuardians:\n"
        for zookeeper in self.zookeepers:
            message += f"\t\t{zookeeper}\n"
        
        return message



class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    

    def add_animal(self, *new_animal):
        if new_animal:
            for each_animal in new_animal:
                if each_animal not in self.animals:
                    self.animals.append(each_animal)
                else:
                    print(f'{each_animal} already exist in the zoo')
        print(', '.join(self.animals))


ny_zoo = Zoo('New York Zoo')
ny_zoo.add_animal('Elephant', 'Emma', 'Appe') #use *args for that
# ny_zoo.add_animal('Emma')
# ny_zoo.add_animal('Appe')
ny_zoo.add_animal('Avestruz')
ny_zoo.add_animal('Emma')


#for the daily challenge: refactor your code to be able to do this:
macdonald.add_animal(cow = 5, sheep = 2, goat = 12)
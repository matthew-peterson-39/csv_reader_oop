import csv
class Pet:
    def __init__(self, animal_type, name, age, breed):
        self._name = name
        self._age = age
        self.animal_type = animal_type
        self.breed = breed

    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self, new_name):
        self._name = new_name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def set_age(self, new_age):
        if str(new_age).isnumeric():
            self._age = new_age
        else:
            return 'Enter a number: '
    
    def __str__(self):
        return f'{self.name} is a {self._age} year old {self.breed} {self.animal_type}'

def file_import(animal_type):
    if animal_type.upper() == 'CAT':
        csv_file = './data/cats.csv'
        new_type = 'cat'
    elif animal_type.upper() == 'DOG':
        csv_file = './data/dogs.csv'
        new_type = 'dog'
    try:
        with open(csv_file, newline='') as csvfile:
            new_file = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in new_file:
                animal_list.append(row)
                # print(' '.join(row))
            for i in range(1, len(animal_list)):
                animal_list[i] = animal_list[i][0].split(',')
                # print(animal_list[i])
                name = animal_list[i][0]
                age = animal_list[i][1]
                breed = animal_list[i][2]
                new_animal = Pet(animal_type=new_type, name=name, age=age, breed=breed)
                print(new_animal)
                print('')
    except ValueError:
        pass
    except FileNotFoundError:
        print('Error cannot find a file with that name.')

        
if __name__ == '__main__':
    animal_list = []
    animal_type = input('Please enter the animal type (dog/cat): ')
    file_import(animal_type)
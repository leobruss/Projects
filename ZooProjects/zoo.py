"""Sistema di gestione dello zoo virtuale

Classi:

1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, 
height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere 
uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. 
I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere 
altri compiti nel nostro zoo virtuale.

Funzionalità:

1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere 
un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat 
e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale 
dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello 
spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di 
nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto
alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale 
si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti 
i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per 
pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. 
Se l'area residua è pari a 0, restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, 
sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale) con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

Guardians:

ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

Fences:

Fence(area=100, temperature=25, habitat=Continent)

with animals:

Animal(name=Scoiattolo, species=Blabla, age=25)

Animal(name=Lupo, species=Lupus, age=14)
#########################

Fra un recinto e l'altro mettete 30 volte il carattere #."""


#1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.
class Zoo:
    def __init__(self, zoo_name: str, zoo_address: str) ->None:
        self.zoo_name = zoo_name
        self.zoo_address = zoo_address
        self.zoo_keeper_name: str[ZooKeeper] = None
        self.zoo_keeper_surname: str[ZooKeeper] = None
        self.id: str[ZooKeeper] = None
        self.area: float[Fence] = None
        self.temperature: float[Fence] = None
        self.habitat: str[Fence] = None
        self.animal_name: str[Animal] = None
        self.species: str[Animal] = None
        self.age: int[Animal] = None
        self.height: float[Animal] = None
        self.width: float[Animal] = None
        self.preferred_habitat: str[Animal] = None
        self.health: float[Animal] = None

        print(f"Welcome to {self.zoo_name} on {self.zoo_address}\n")
        
    def describe_zoo(self):

        '''print(f"Guardians:\n","name=",self.zoo_keeper_name, "surname=",self.zoo_keeper_surname, "id=",self.id)
        print()
        print(f"Fenece:\n","fence=",self.area, "temperature=",self.temperature,"°", "habitat=",self.habitat)
        print() 
        print(f"with animals:\n","name=",self.animal_name, "species=",self.species, "age=",self.age, "height=",self.height, "width=",\
              self.width, "preferred habitat=",self.preferred_habitat, "health=",self.health)'''
        
       


#2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, 
#height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).
class Animal:
    def __init__(self, animal_name: str, species: str , age: int, height: float, width: float, preferred_habitat: str, health: float) -> None:
        self.animal_name: str = animal_name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health = health = round(100 * (1 / age), 3)

    def get_area(self):
        animal_area: float = self.width * self.height



#3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere 
#uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.
class Fence:
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []   

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def get_free_area(self):
        fence_occuped_area: int = 0
        for animal in self.animals:
            fence_occuped_area += animal.get_area()



    
#4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. 
#I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere 
#altri compiti nel nostro zoo virtuale.
class ZooKeeper:
    def __init__(self, zoo_keeper_name: str, zoo_keeper_surname: str, id: str) -> None:
        self.zoo_keeper_name: str = zoo_keeper_name
        self.zoo_keeper_surname: str = zoo_keeper_surname
        self.id: str = id

    def add_animal(self, animal: Animal, fence: Fence)->None:
        
        if animal.preferred_habitat == fence.habitat and fence.get_free_area >= animal.get_area:
            fence.animals.append(animal)
            fence.area = fence.area - fence.get_free_area
        elif animal.preferred_habitat == fence.habitat and fence.get_free_area < animal.get_area:
            print("Sorry, but we have not more space here")
        elif animal.preferred_habitat != fence.habitat:
            print("This animal can't live here!")



 
z1: Zoo = Zoo("Zoo", "Via dello Zoo")
animal1: Animal = Animal("Lion", "mammal", 15, 1.2, 2, "Savannah", 5)
fence1: Fence = Fence(10, 37, "Savannah")
fence1.add_animal(animal1)
print("Zoo name: ", z1.zoo_name)
print("Zoo Address: ", z1.zoo_address)
print()
'''#Zoo Keeper Info
z1.zoo_keeper_name = "Max"
z1.zoo_keeper_surname = "Smith"
z1.id = "246082"
#Fence Info
z1.area = 10
z1.temperature = 37
z1.habitat = "Savannah"
#Animals Info
z1.animal_name = "Lion"
z1.species = "mammal"
z1.age = 15 
z1.height = 1.2
z1.width = 2
z1.preferred_habitat = "Savannah"
z1.health = 5'''
z1.describe_zoo()




'''1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere 
un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat 
e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale 
dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello 
spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di 
nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto
alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale 
si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti 
i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per 
pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. 
Se l'area residua è pari a 0, restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, 
sui recinti dello zoo che contengono animali.'''

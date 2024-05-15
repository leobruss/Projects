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
        self.fences: list[Fence] = []
        self.zoo_keepers: list[ZooKeeper] = []

        
        
    def describe_zoo(self):
        for k in self.zoo_keepers:
            print("Guardians:")
            print(f"ZooKeeper(name={k.zoo_keeper_name}, surname={k.zoo_keeper_surname}, id={k.id})\n")
            for time in k.fences:
               time_to_clean = k.clean()
               print(f"Time to clean {time.habitat} fence: {time_to_clean} hours")
        for f in self.fences:
            print("Fences:")
            print()
            print(f"Fence(area={f.area:.2f}, temperature={f.temperature}, habitat={f.habitat})")
            print()
            print("Whith animals")
            print()
            for a in f.animals:
                 print(f"Animal(name={a.animal_name}, species={a.species}, age={a.age})\n")
            print("#" * 30)
            for t in f.time:
                print("Time to cloean the fence:")
                print(f"The time it took to clean was {t.clean}")




        
       


#2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, 
#height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).
class Animal:
    def __init__(self, animal_name: str, species: str , age: int, height: float, width: float, preferred_habitat: str) -> None:
        self.animal_name: str = animal_name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health = round(100 * (1 / age), 3)

    def get_area(self):
        animal_area: float = self.width * self.height
        return animal_area



#3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere 
#uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.
class Fence:
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []   
        self.time: list[ZooKeeper] = []


    def get_free_area(self):
        fence_free_area: int = self.area
        for animal in self.animals:
            fence_free_area -= animal.get_area()
        return fence_free_area


    
#4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. 
#I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere 
#altri compiti nel nostro zoo virtuale.
class ZooKeeper:
    def __init__(self, zoo_keeper_name: str, zoo_keeper_surname: str, id: str) -> None:
        self.zoo_keeper_name: str = zoo_keeper_name
        self.zoo_keeper_surname: str = zoo_keeper_surname
        self.id: str = id
        self.fences: list[Fence] = []
        


    def add_animal(self, animal: Animal, fence: Fence)->None:
        
        if animal.preferred_habitat == fence.habitat and fence.get_free_area() >= animal.get_area():
            fence.animals.append(animal)
        elif animal.preferred_habitat == fence.habitat and fence.get_free_area() < animal.get_area():
            print(f"Sorry, but we have not more space for the {animal.animal_name} in {fence.habitat}! ")
        elif animal.preferred_habitat != fence.habitat:
            print(f"\'{animal.animal_name}\'This animal can't live in {fence.habitat}!")

    def remove_animal(self, animal: Animal, fence: Fence) ->None:
        if animal in fence.animals:
            fence.animals.remove(animal)
          
        else:
            print("Animal not in this fence")
        
    def feed(self, animal: Animal) ->None:
        for fence in self.fences:
            if animal in fence.animals:
                if fence.get_free_area() >= animal.get_area() * 2 / 100:
                    animal.health += animal.health * 1 / 100
                    animal.get_area += animal.get_area* 2 / 100
                else:
                    print(f"Sorry, but we have not more space for the {animal.animal_name} in {fence.habitat}! ")
                    break
            else:
                print(f"{animal.animal_name} is not in any of the fences.")
    
    def clean(self, fence: Fence) ->float:
        for fence in self.fences:
            if fence.get_free_area() > 0:
                time_to_clean = (fence.area - fence.get_free_area)/ fence.get_free_area
                fence.time.append(time_to_clean)
            else:
                fence.time.append(fence.get_free_area)
        return time_to_clean


                    

        




z1: Zoo = Zoo("Zoo", "Via dello Zoo")

#Liste di animal
animal1: Animal= Animal("Lion", "mammal", 15, 1.2, 2, "Savannah")
animal2: Animal= Animal("Tiger", "mammal", 10, 0.8, 1.1, "Rain forest")
animal3: Animal= Animal("Elephant", "mammal", 25, 2, 6.5, "Savannah")


#Liste di fence
fence1: Fence = Fence(15, 37, "Savannah")
fence2: Fence = Fence(8, 27, "Rain forest")

z1.fences.append(fence1)
z1.fences.append(fence2)
#Liste di zoo keepers

zoo_keeper1: ZooKeeper = ZooKeeper("Max", "Smith", 2648)

#Unione tra animali e dei rispettivi recinti
zoo_keeper1.add_animal(animal1, fence1)
zoo_keeper1.add_animal(animal2, fence2)
zoo_keeper1.add_animal(animal3, fence1)
#Rimozione degli animali dal loro rispettivo recinto
zoo_keeper1.remove_animal(animal2, fence2)
z1.zoo_keepers.append(zoo_keeper1)





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

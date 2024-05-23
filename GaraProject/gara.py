import random
print("BANG !!!!! AND THEY'RE OFF !!!!!")
def position(tartaruga_position: int, lepre_position: int, meteo: str) -> list:
    lenght_list = 70
    competition: list= ["_"] * lenght_list
    

    if meteo == "Sole":
        print("Today there is the sun")
    elif meteo == "Pioggia":
        print("Today it's raining")
        if tartaruga_position > 1:
            tartaruga_position -= 1
        else:
            pass
        if lepre_position > 2:
            lepre_position -= 2
        else: 
            pass
    if tartaruga_position == lepre_position :
        competition[tartaruga_position] = 'OUCH!!!'
        print("".join(competition))
    elif tartaruga_position >= 69 and lepre_position >= 69:
        competition[-1] = 'T'
        competition[-1] = 'H'
        print("".join(competition))
        print("Tie!!")
    elif tartaruga_position >= 69:
        competition[-1] = 'T'
        competition[lepre_position] = 'H'
        print("".join(competition))
        print("TORTOISE WINS! || VAY!!!")
    elif lepre_position >= 69:
        competition[tartaruga_position] = 'T'
        competition[-1] = 'H'
        print("".join(competition))
        print("HARE WINS || YUCH!!!")
    else:
        competition[tartaruga_position] = 'T'
        competition[lepre_position] = 'H'
        print("".join(competition))
    
    

def tartaruga(last_position_t: int) -> int:
    i = random.randint(1, 10)
    t_stamina = 100
    ostacoli: dict = {
        15 : 3,
        30 : 4,
        45 : 7,
        60 : 9
    } 
    bonus: dict ={
        10 : 3,
        25 : 4,
        50 : 9,
        65 : 3
    }
    
    # Calcolo del movimento della tartaruga e della stamina rimanente
    if t_stamina >= 10:
        if 1 <= i <= 5:
            last_position_t += 3
            t_stamina -= 5
        elif 6 <= i <= 7:
            if last_position_t <= 6:
                last_position_t = 1
            else: 
                last_position_t -= 6
                t_stamina -= 10
        elif 8 <= i <= 10:
            last_position_t += 1
            t_stamina -= 3
    else:
        t_stamina += 5
    print()
    print("stamina tartaruga: ", t_stamina)

    #Calcolo della posizione della tartaruga in caso di ostacolo
    if last_position_t in ostacoli:
        if last_position_t >= ostacoli[last_position_t]:
            print(f"T penalità in ostacolo: {last_position_t}")
            last_position_t -= ostacoli[last_position_t]
        else:
            last_position_t = 0
            print("T penalità, posizione tornata a 0")  

    #Calcolo della posizione della tartaruga in caso di bonus
    if last_position_t in bonus:
        if last_position_t >= bonus[last_position_t]:
            print(f"T bonus in posizione: {last_position_t}")
            last_position_t += bonus[last_position_t]
        if last_position_t > 70:
            last_position_t == 70       
    return last_position_t
        
            


def lepre(last_position_h: int) -> int:
    i = random.randint(1, 10)
    l_stamina = 100
    ostacoli: dict = {
        15 : 3,
        30 : 4,
        45 : 7,
        60 : 9
    } 
    bonus: dict ={
        10 : 3,
        25 : 4,
        50 : 9,
        65 : 3
    }

    # Calcolo del movimento della lepre e della stamina rimanente
    if  1<= i <= 2:
        l_stamina += 10
        pass
    elif 3 <= i <= 4:
        last_position_h += 9
        l_stamina -= 15
    elif i == 5:
        if last_position_h <= 12:
            last_position_h = 1
            l_stamina -=20
        else: 
            last_position_h -= 12
            l_stamina -=20
    elif 6 <= i <= 8:
        last_position_h += 1
        l_stamina -= 5
    elif 9 <= i <= 10:
        if last_position_h <= 2:
            last_position_h = 1
            l_stamina -= 8
        else: 
            last_position_h -= 2
            l_stamina -= 8
    print("stamina lepre: ", l_stamina)

    #Calcolo della posizione della lepre in caso di ostacolo
    if last_position_h in ostacoli:
        print(ostacoli[last_position_h])
        if last_position_h >= ostacoli[last_position_h]:
            print(f"H penalità in ostacolo: {last_position_h}")
            last_position_h -= ostacoli[last_position_h]
            print(f"H  in ostacolo: {last_position_h}")
        else:
            last_position_h = 0
            print("H penalità, posizione tornata a 0") 

    #Calcolo della posizione della lepre in caso di bonus
    if last_position_h in bonus:
        if last_position_h >= bonus[last_position_h]:
            print(f"H bonus in posizione: {last_position_h}")
            last_position_h += bonus[last_position_h]
        if last_position_h > 70:
            last_position_h == 70  
    return last_position_h

t = 0
h = 0
counter = 0
meteo = "Sole"
while True:
    t = tartaruga(t)
    h = lepre(h)
    counter += 1
    if counter % 10 == 0:
        i = random.randint(1, 2)
        if i == 1:
            meteo = "Sole"
        else:
            meteo = "Pioggia"
    

    print(counter,"° lancio")
    
    (position(t, h, meteo))
    if t >= 69 or h >= 69:
        break

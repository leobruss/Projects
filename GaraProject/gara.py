import random
print("BANG !!!!! AND THEY'RE OFF !!!!!")
def position(tartaruga_position: int, lepre_position: int) -> list:
    lenght_list = 70
    competition: list= ["_"] * lenght_list

    
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
    if 1 <= i <= 5:
        last_position_t += 3
    elif 6 <= i <= 7:
        if last_position_t <= 6:
            last_position_t = 1
        else: 
            last_position_t -= 6
    elif 8 <= i <= 10:
        last_position_t += 1

    return last_position_t
        
            


def lepre(last_position_h: int) -> int:
    i = random.randint(1, 10)
    if  1<= i <= 2:
        pass
    elif 3 <= i <= 4:
        last_position_h += 9
    elif i == 5:
        last_position_h += 1
    elif 6 <= i <= 8:
        last_position_h += 1
    elif 9 <= i <= 10:
        if last_position_h <= 2:
            last_position_h = 1
        else: 
            last_position_h -= 2
    return last_position_h

t = 0
h = 0
counter = 0
while True:
    t = tartaruga(t)
    h = lepre(h)
    counter += 1
    print(counter)
    (position(t, h))
    if t >= 69 or h >= 69:
        break

import random as rd
monsters = []
for i in range(5):
  temp = []
  for i in range(5):
    temp.append(rd.randint(0,9))
  monsters.append(temp)
#print(monsters)

def sex(monster1,monster2):
  newmon = []
  for i in range(5):
    mut = rd.randint(0,101)
    #print(mut)
    if mut > 93:
      newmon.append(rd.randint(0,9))
    else:
      gen = rd.randint(0,10)
      #print(gen)
      if gen <4:
        newmon.append(monster1[i])
      else:
        newmon.append(monster2[i])
  monsters.append(newmon)
#print(monsters[1],monsters[2])
#sex(monsters[1],monsters[2])
#print(monsters)

def rd_pair(singlemons:list)->list:
    x = rd.randint(0,len(singlemons)-1)
    y = x
    pair = []
    while y==x:
        y = rd.randint(0,len(singlemons)-1)
    pair.append(x)
    pair.append(y)
#    print(pair)
    return pair

def iq_test(monster:list)->int:
   #print (monster.count(1))
   return monster.count(1)

def filling(monsters):
    for i in range(10-len(monsters)):
        x = rd_pair(monsters)
        sex(monsters[x[0]],monsters[x[1]])
#print(monsters)
def drop_out(monsters):
    ar_avarage = 0
    p = 0
    for i in monsters:
        ar_avarage+= int(iq_test(i))
        p +=1
    avarage = ar_avarage/p
    min_count = avarage
    poppin = []
    position = 0
    for i in monsters:
        if iq_test(i) < min_count:
            poppin.append(position)
        elif iq_test(i) >min_count:
            position += 1


    if position ==0:
        for i in range(5):
            monsters.pop(i)

    for i in poppin:
        if len(monsters)>2:
            monsters.pop(i)
print(monsters)
for i in range(50):
    filling(monsters)
    print(monsters)
    drop_out(monsters)
    print(monsters)

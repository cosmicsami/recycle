import random,pgzrun
WIDTH=600
HEIGHT=600
ITEMS=["bag","battery","bottle","crisps"]
level=1
actors=[]
animation=[]


def picker(level):
    objects=["paper"]
    for i in range(level):
        objects.append(random.choice(ITEMS))
    return objects
def making_actors(objects):
    actors=[]
    for i in objects:
        actors.append(Actor(i+"img"))
    return actors
def layout(actors):
    nog=len(actors)+1
    gap_size=WIDTH//nog
    for i,v in enumerate (actors):
        v.pos=(I+1)*gap_size,0

pgzrun.go()
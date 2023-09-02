import random


def is_intersecting(rect1, rect2):
    return rect1.colliderect(rect2)


def fight(colony_a, colony_b):
    for ant_a in colony_a.ants:
        for ant_b in colony_b.ants:
            if is_intersecting(ant_a.rect, ant_b.rect):
                winner = random.randint(0, 1)
                if winner == 0:
                    if ant_a in colony_a.ants:
                        colony_a.ants.remove(ant_a)
                else:
                    if ant_b in colony_b.ants:
                        colony_b.ants.remove(ant_b)

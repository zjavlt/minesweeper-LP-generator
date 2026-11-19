import math
import random

def calculate_distance(a: tuple[int], b: tuple[int]):
    y1, x1 = a
    y2, x2 = b
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def calculate_score(node:tuple[int], peaks:list[tuple[int]], rate):
    mini = 1e9
    for point in peaks:
        mini = min(mini, calculate_distance(node, point))
    return mini * rate
    return random.normalvariate(0, mini * rate)
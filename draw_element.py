import random
from generate_lists import data

def draw_element(arr: list[int]):
    element_choice = random.choice(arr)
    return element_choice

element_1_000 = draw_element(data[1_000])
element_10_000 = draw_element(data[10_000])
element_50_000 = draw_element(data[50_000])
element_100_000 = draw_element(data[100_000])

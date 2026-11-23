import random

def generate_lists() -> dict[int, list[int]]:
    sizes = [1_000, 10_000, 50_000, 100_000]
    
    return {
        n: list(random.sample(range(n * 10), n))
        for n in sizes        
    }
    
data = generate_lists()

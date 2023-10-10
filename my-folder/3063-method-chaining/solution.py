import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    heavy_animals = animals[animals['weight'] > 100]
    sorted_heavy_animals = heavy_animals.sort_values(by='weight', ascending=False)
    animal_name = sorted_heavy_animals[['name']]
    return animal_name


import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    res = products[(products["low_fats"] == 'Y') & (products["recyclable"] == 'Y')]
    return res[['product_id']]

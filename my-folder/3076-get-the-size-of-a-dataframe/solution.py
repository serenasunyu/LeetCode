import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = pd.DataFrame(players)
    result = [df.shape[0], df.shape[1]]
    return result

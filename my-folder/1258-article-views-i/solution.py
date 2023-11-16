import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    unique_authors = df[['author_id']].rename(columns={'author_id' : 'id'}).drop_duplicates().sort_values('id')
    return unique_authors

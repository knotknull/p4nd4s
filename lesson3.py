"""
Lesson 3 of pandas tutorial:  Summary Funcs and Maps
"""
import pandas as pd


def stars(row) -> int:
    """
    stars function to convert points to stars
    """
    if row.country == 'Canada':
        return 3
    if row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

def l3_sum() -> None:
    ## get summary on a dataframe
    reviews = pd.read_csv('./data/winemag-data-130k-v2.csv')
    pd.set_option('display.max_columns', 5)
    
    ## Summary Functions    
    print("[[ reviews.points.describe() ]]\n ",reviews.points.describe())              ## get summary stats on points
    print("[[ reviews.points.mean() ]]\n ",reviews.points.mean())                      ## get mean stats on points
    print("[[ reviews.taster_name.describe() ]]\n ",reviews.taster_name.describe())    ## get stats on taster_name
    print("[[ reviews.taster_name.unique() ]]\n ",reviews.taster_name.unique())        ## get stats on taster_name
    print("[[ reviews.taster_name.value_counts() ]]\n ",reviews.taster_name.value_counts())        ## get stats on taster_name
    
    ## Map Functions:  takes in a serires and returns a new transformed series    
    review_points_mean = reviews.points.mean()
    print("[[ reviews.points.map() ]]\n ",reviews.points.map(lambda p: p - review_points_mean))        ## get stats on taster_name

    ## apply returns a transformed dataset 
    ## reviews.apply(remean_points, axis='columns')
    mean_points= reviews.points - review_points_mean
    print("[[ mean_points ]]\n ", mean_points )        ## apply transforms the entire dataset


    ## map tropical and fruity
    n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
    n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
    descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
    print("[[ descriptor_counts ]]\n ", descriptor_counts)

    star_ratings = reviews.apply(stars, axis='columns') 
    print("[[ star_ratings ]]\n ", star_ratings.loc[reviews.country.isin(['Canada'])])
    ## print("reviews.loc[reviews.country.isin(['Australia', 'New Zealand']) & (reviews.points >= 95)]", 
    ## reviews.loc[reviews.country.isin(['Australia','New Zealand']) & (reviews.points >= 95)])   # query countries and price
    print("[[ star_ratings ]] ", star_ratings.iloc[:100])     # get specific rows with columns     
    print("[[ star_ratings.shape ]] ", star_ratings.shape)     # get specific rows with columns     
    
    return None

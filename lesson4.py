"""
Lesson 3 of pandas tutorial:  Summary Funcs and Maps
"""

import pandas as pd


def stars(row) -> int:
    """
    stars function to convert points to stars
    """
    if row.country == "Canada":
        return 3
    if row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1


def l4_group() -> None:
    ## get summary on a dataframe
    reviews = pd.read_csv("./data/winemag-data-130k-v2.csv")
    # pd.set_option("display.max_columns", 5)

    ## group by points and get counts for each points entry
    ## NOTE: value_counts() is a shortcut for groupby and count

    print(
        "[[ reviews.groupby('points').points.count()) ]]\n ",
        reviews.groupby("points").points.count(),
    )

    ## get min pirce at each point level
    print(
        "[[ reviews.groupby('points').price.min()), max() ]]\n ",
        reviews.groupby("points").price.min(),
        reviews.groupby("points").price.max(),
    )

    return None


def l4_group_apply() -> None:
    reviews = pd.read_csv("./data/winemag-data-130k-v2.csv")
    ## get first title for each winery
    print(
        "reviews.groupby('winery').apply(lambda df: df.title.iloc[0])",
        reviews.groupby("winery").apply(lambda df: df.title.iloc[0]),
    )

    ## group by country and provice and return highest point wine
    ## get best wine for each country, province
    print(
        " reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]",
        reviews.groupby(["country", "province"]).apply(
            lambda df: df.loc[df.points.idxmax()]
        ),
    )
    return None


def l4_group_agg() -> None:
    reviews = pd.read_csv("./data/winemag-data-130k-v2.csv")
    ## agg is a groupby function that runs multiple functions on a group simultaneously
    print(
        "reviews.groupby(['country']).price.agg([len, min, max])",
        reviews.groupby(["country"]).price.agg([len, min, max]),
    )
    return None

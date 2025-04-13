"""
Lesson 1 of pandas tutorial
"""

import pandas as pd


def l1_create_df() -> None:
    ## Dataframe is a dictionary.  Keys are column names and values are a list entries
    ##
    df = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
    print(df)
    #    Yes   No
    # 0   50  131
    # 1   21    2

    # Another way is to create the data and columns separately
    df = pd.DataFrame([[50, 21], [131, 2]], columns=["Yes", "No"])
    print(df)

    # FYI: row labeels are an index and can be assigned
    sdf = pd.DataFrame(
        {"Bob": ["I liked it", "It was awful"], "Sue": ["Pretty good", "Bland"]},
        index=["Product A", "Product B"],
    )
    print(sdf)
    #                    Bob          Sue
    # Product A    I liked it  Pretty good
    # Product B  It was awful        Bland

    return None


def l1_create_ser() -> None:
    ## Create a series, a sequence of data values (i.e. a list of values)
    ## NOTE: a series is a single column df
    ##
    s = pd.Series([1, 2, 3, 4, 5])
    print(s)

    ## Can assign row label to a series via Index (as above)
    sidx = pd.Series(
        [30, 35, 44], index=["2015 Sales", "2016 Sales", "2017 Sales"], name="Product X"
    )
    print(sidx)

    return None


def l1_read_wine() -> None:
    wine_revs = pd.read_csv("./data/wine/winemag-data-130k-v2.csv")
    print("head : ", wine_revs.head())
    print("shape: ", wine_revs.shape)

    ## use the index within the file itself and designate it
    wine_revs = pd.read_csv("./data/wine/winemag-data-130k-v2.csv", index_col=0)
    print("head : ", wine_revs.head())
    return None


def l1_write_wine() -> None:
    # read it in and then
    print("<<  l1_write_wine()  >>")
    wine_revs = pd.read_csv("./data/wine/winemag-data-130k-v2.csv", index_col=0)
    print("wine_revs.shape: \n", wine_revs.shape)

    print("write out to data/wine/map_wine_reviews.csv")
    wine_revs.to_csv("./data/wine/map_wine_reviews.csv")

    ## read in written file out
    map_revs = pd.read_csv("./data/wine/map_wine_reviews.csv", index_col=0)
    print("map_revs.shape : \n", map_revs.shape)
    print("map_revs.head(): \n", map_revs.head())

    return None

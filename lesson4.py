"""
Lesson 3 of pandas tutorial: Summary Funcs and Maps
"""

import pandas as pd


class WineReviews:
    def __init__(self, csv_path: str):
        """
        Initialize the WineReviews class with a shared DataFrame.
        """
        self.csv_path = csv_path
        self.reviews = self.get_reviews()

    def get_reviews(self) -> pd.DataFrame:
        """
        Load reviews from the CSV file.
        """
        return pd.read_csv(self.csv_path)

    def group(self) -> None:
        """
        Group by points and get counts, min, and max prices.
        """
        print(
            "[[ reviews.groupby('points').points.count()) ]]\n ",
            self.reviews.groupby("points").points.count(),
        )

        print(
            "[[ reviews.groupby('points').price.min()), max() ]]\n ",
            self.reviews.groupby("points").price.min(),
            self.reviews.groupby("points").price.max(),
        )

    def group_apply(self) -> None:
        """
        Apply custom functions to grouped data.
        """
        print(
            "reviews.groupby('winery').apply(lambda df: df.title.iloc[0])",
            self.reviews.groupby("winery").apply(lambda df: df.title.iloc[0]),
        )

        print(
            "reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]",
            self.reviews.groupby(["country", "province"]).apply(
                lambda df: df.loc[df.points.idxmax()]
            ),
        )

    def group_agg(self) -> None:
        """
        Use agg to run multiple functions on grouped data.
        """
        print(
            "reviews.groupby(['country']).price.agg([len, min, max])",
            self.reviews.groupby(["country"]).price.agg([len, min, max]),
        )

    def multi_idx(self) -> None:
        """
        Create and manipulate a multi-index DataFrame.
        """
        cp_agg = self.reviews.groupby(["country", "province"]).description.agg([len])
        print("cp_agg.groupby(['country']).price.agg([len]) \n", cp_agg)

        mi = cp_agg.index
        print("type(cp_agg.index) \n", type(mi))
        print("cp_agg.index \n", mi)

        cp_agg = cp_agg.reset_index()
        print("cp_agg.reset_index() \n", cp_agg)

    def sorted(self) -> None:
        """
        Sort values in the DataFrame.
        """
        cp_agg = self.reviews.groupby(["country", "province"]).description.agg([len])
        cp_agg = cp_agg.reset_index()

        print("cp_agg.sort_values(by='len') \n", cp_agg.sort_values(by="len"))

        print(
            "cp_agg.sort_values(by='len', ascending=False) \n",
            cp_agg.sort_values(by="len", ascending=False),
        )

    def sortby(self) -> None:
        """
        Sort by index or multiple columns.
        """
        cp_agg = self.reviews.groupby(["country", "province"]).description.agg([len])
        cp_agg = cp_agg.reset_index()

        print("cp_agg.sort_index() \n", cp_agg.sort_index())

        print(
            "cp_agg.sort_values(by=['country', 'len']) \n",
            cp_agg.sort_values(by=["country", "len"]),
        )


# Example usage:
# wine_reviews = WineReviews("./data/winemag-data-130k-v2.csv")
# wine_reviews.group()
# wine_reviews.group_apply()
# wine_reviews.group_agg()
# wine_reviews.multi_idx()
# wine_reviews.sorted()
# wine_reviews.sortby()

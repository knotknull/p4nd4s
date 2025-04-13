"""
Concat, join, merge pandas functions
"""

import pandas as pd


class Combine:
    def __init__(self):
        """
        Initialize the Combine class with multiple dataframes
        """
        self.ca_vids = self.get_videos("./data/youtube/CAvideos.csv")
        self.uk_vids = self.get_videos("./data/youtube/GBvideos.csv")
        self.all_vids = self.combine_vids()

    def get_videos(self, vid_path) -> pd.DataFrame:
        """
        Load reviews from the CSV file.
        """
        return pd.read_csv(vid_path)

    def combine_vids(self) -> pd.DataFrame:
        """
        Combine the ca_vids and uk_vids
        """
        ## return pd.concat([self.ca_vids, self.uk_vids], ignore_index=True)
        return pd.concat([self.ca_vids, self.uk_vids])

    def show_shapes(self) -> None:
        print(
            "\n\nself.ca_vids.shape: \n ",
            self.ca_vids.shape,
            "\n\nself.uk_vids.shape: \n ",
            self.uk_vids.shape,
            "\n\nself.all_vids.shape: \n ",
            self.all_vids.shape,
        )
        return None

    def joiner(self) -> None:
        """
        Data type of field / fields
        """
        left = self.ca_vids.set_index(["title", "trending_date"])
        right = self.uk_vids.set_index(["title", "trending_date"])
        left.join(right, lsuffix="_CAN", rsuffix="_UK")
        print(
            "\n\nleft.shape: \n ",
            left.shape,
            "\n\nleft: \n ",
            left,
        )
        return None


# Example usage:
# combo = Combine()
# combo.group()
# combo.group_apply()
# combo.group_agg()
# combo.multi_idx()
# combo.sorted()
# combo.sortby()

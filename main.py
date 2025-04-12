import lesson1 as l1
import lesson2 as l2
import lesson3 as l3
from lesson4 import WineReviews


def main():
    print("Hello from p4nd4s!")
    # l1.l1_create_df()
    # l1.l1_create_ser()
    # l1.l1_read_wine()
    # l1.l1_write_wine()

    # l2.l2_read_df()
    # l2.l2_index()
    # l2.l2_loc()
    # l2.l2_assign()

    # l3.l3_sum()

    ## Use class version
    wine_reviews = WineReviews("./data/winemag-data-130k-v2.csv")
    # wine_reviews.group()
    # wine_reviews.group_apply()
    # wine_reviews.group_agg()
    # wine_reviews.multi_idx()
    # wine_reviews.sorted()
    # wine_reviews.sortby()

    ## data types and missing values
    wine_reviews.show_dtypes()
    wine_reviews.show_astype()

    ## show null / not null
    wine_reviews.show_null_country()
    wine_reviews.fill_missing()
    wine_reviews.replace_val()


if __name__ == "__main__":
    main()

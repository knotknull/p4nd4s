"""
Lesson 2 of pandas tutorial 
"""
import pandas as pd


def l2_read_df() -> None:
    reviews = pd.read_csv('./data/winemag-data-130k-v2.csv')
    pd.set_option('display.max_columns', 5)
    print('shape: ', reviews.shape)
    print('reviews: ', reviews)
    
    ## access dataframe by property 
    print('country: ', reviews.country)
    
    ## or indexing operator
    print('country: ', reviews['country'])
    
    ## access a specific entry
    print('      0: ', reviews['country'][0])
    print('     10: ', reviews['country'][10])
    print('    100: ', reviews['country'][100])
    print('   1000: ', reviews['country'][1000])
    print('  10000: ', reviews['country'][10000])
    print(' 100000: ', reviews['country'][100000])

    
    return None

def l2_loc() -> None:
    reviews = pd.read_csv('./data/winemag-data-130k-v2.csv')

    ## get data by index-based position
    print('iloc[0]: ', reviews.iloc[0]) 
    
    ## loc and iloc are row-first, column-second  
    ## iloc index based location
    print('iloc[:,1]', reviews.iloc[:, 1])      # This gets all rows and the first column
    print('iloc[:4,1]', reviews.iloc[:4, 1])    # This gets first five rows and the first column
    print('iloc[[98,99,100],1]', reviews.iloc[[98,99,100], 1])   # pass a lsit
    print('iloc[-5:]', reviews.iloc[-5:])       # hey look negative numbers!! starts from end and works backward
    
    ## loc index location
    print("loc[[0,1,10,100],['country','province','region_1','region_2']]", 
            reviews.loc[[0,1,10,100],['country','province','region_1','region_2']])     # get specific rows with columns
    
    ## loc by value (i.e. like a query ) 
    
    print("reviews.loc[reviews.country == 'Italy']", 
            reviews.loc[reviews.country == 'Italy'])       # query Italy 
    
    print("reviews.loc[reviews.country.isin(['Australia', 'New Zealand']) & (reviews.points >= 95)]", 
            reviews.loc[reviews.country.isin(['Australia','New Zealand']) & (reviews.points >= 95)])   # query countries and price
    
    print("reviews.loc[reviews.price.notnull()]", 
            reviews.loc[reviews.price.notnull()])   # not null prices
    
    print("reviews.loc[reviews.price.isnull()]", 
            reviews.loc[reviews.price.isnull()])   # null prices
    return None

def l2_assign() -> None:
    reviews = pd.read_csv('./data/winemag-data-130k-v2.csv')
    reviews['critic'] = 'everyone'      ## constant value assigned to all rows
    print("reviews['critic'] : " , reviews['critic'])
    
    reviews['backwards_idx'] = range(len(reviews),0,-1)     ## backwards iteration   
    print("reviews['backwards_idx'] : " , reviews['backwards_idx'])
    
    return None
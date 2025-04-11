"""
Lesson 1 of pandas tutorial 
"""
import pandas as pd


def l1_create_df() -> None:
    ## Dataframe is a dictionary.  Keys are column names and values are a list entries
    ##
    df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
    print(df)  
    #    Yes   No
    # 0   50  131
    # 1   21    2
    
    # Another way is to create the data and columns separately 
    df = pd.DataFrame([[50, 21],[131,2]], columns=['Yes','No'])
    print(df)  
    
    # FYI: row labeels are an index and can be assigned 
    sdf = pd.DataFrame({'Bob': ['I liked it', 'It was awful'], 
                        'Sue': ['Pretty good', 'Bland']},
                       index=['Product A', 'Product B'])
    print(sdf)  
                        Bob          Sue
    # Product A    I liked it  Pretty good
    # Product B  It was awful        Bland
    
    return None

def l1_create_ser() -> None:
    ## Create a series, a sequence of data values (i.e. a list of values)
    ## NOTE: a series is a single column df 
    ##
    s=pd.Series([1, 2, 3, 4, 5])
    print(s)
    
    ## Can assign row label to a series via Index (as above)  
    sidx=pd.Series([30, 35, 44], index=['2015 Sales', '2016 Sales', '2017 Sales' ], name= 'Product X')
    print(sidx)
    
    return None

def l1_read_wine() -> None:
    return None
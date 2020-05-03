import numpy as np
import pandas as pd



schema = pd.DataFrame()

def get_description(column_name, schema=schema):
    '''
    INPUT:
        schema - pandas dataframe with the schema of waterbase
        column_name - string - the name of the column you would like to know about
    OUTPUT:
        desc - string - the description of the column
    '''
    
    desc = list(schema[schema['Id'] == column_name]['Label'])[0]
    return desc


def categorical_profile(df, category_list, top_categ, normalize=True):
    '''
    INPUT:
        df - pandas dataframe with the data from the waterbase
        category_list - list of categorical variables to profile
        top_categ - top number of categories to show
        normalize - False to include Nulls or NAN
    OUTPUT:
        pandas dataframe with the list of categorical variables and respective percentage
            for each category in ascending order with top10 categories if more than 10
    '''
    # Create an empty DataFrame for the profile table
    profile = pd.DataFrame()
    
    # Create a DataFrame with the percentage for each category 
    for i in category_list:
        if normalize:
            catg_perc= df[i].value_counts(normalize=True).sort_values(ascending=False)*100 # Relative, No nulls
        #catg_perc= df[i].value_counts().sort_values(ascending=False)/df.shape[0]*100 # Overall
        else:
            catg_perc= df[i].value_counts().sort_values(ascending=False)

        # Select the top in categories to display
        catg_top = catg_perc[:top_categ].sort_values(ascending=False)
        catg_topi = catg_top.index
        

        #Create a dataframe with multiple index:
        catg_list = [i]*top_categ
        tuples = list(zip(catg_list, catg_topi))
        catg_df = pd.DataFrame({'Percentage(%)' : catg_top.values}, 
                               index = pd.MultiIndex.from_tuples(tuples, names=['Group', 'Sub-Group']))
        

        profile = profile.append(catg_df).round(2)
    
    return profile
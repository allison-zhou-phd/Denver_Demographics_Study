import numpy as np
import pandas as pd

def import_data(filepath, col_lst, sort_col):
    '''
    for given filepath, read in data and return df of columns of interest, sorted by sort_col
    '''
    df_raw = pd.read_csv(filepath, na_values='None')
    df_out = df_raw[col_lst].sort_values(sort_col, ascending = True)
    return df_out

def calc_data(df):
    '''
    take in a df and return the df with additional calculated col. This assumes referenced col are in the df 
    '''
    df.eval('SCH_AGE = AGE_5_TO_9 + AGE_10_TO_14 + AGE_15_TO_17', inplace=True)
    df.eval('AGE_18_65 = TTL_POPULATION_ALL - AGELESS18 - AGE65PLUS', inplace=True)
    df.eval('HOUSE_AFFORD = MEDIAN_HOME_VALUE / MED_HH_INCOME', inplace=True)
    return df


if __name__ == "__main__":
    file_lst = ['2014_2018']
    col_lst = (['STFID','TTL_POPULATION_ALL','MALE','FEMALE','AGE_LESS_5','AGE_5_TO_9','AGE_10_TO_14', 
             'AGE_15_TO_17','AGELESS18','AGE65PLUS','MEDIAN_AGE_ALL', 'MEDIAN_AGE_MALE','MEDIAN_AGE_FEMALE','TTLPOP_25PLUS_EDU', 
             'TTLPOP_25PLUS_EDU_MOE','LESS_THAN_HS_DIPLOMA_EDU','HSGRAD_OR_EQUIV_EDU','SOMECOLLEGE_OR_AA_EDU','BACHELORS_OR_HIGHER_EDU', 
             'TTL_HOUSING_UNITS','OCCUPIED_HU','MED_HH_INCOME','AVG_HH_INCOME','MEDIAN_EARNINGS','MEDIAN_EARN_MALE','MEDIAN_EARN_FEMALE', 
             'MED_CONTRACT_RENT','MEDIAN_HOME_VALUE'])
    for file in file_lst:
        file_path = 'data/american_community_survey_blk_grp_'+file+'.csv'
        df = import_data(file_path, col_lst, 'STFID')
        df = calc_data(df)


    

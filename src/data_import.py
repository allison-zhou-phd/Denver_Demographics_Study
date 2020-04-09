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
    df.eval('SCH_AGE_PC = SCH_AGE / TTL_POPULATION_ALL', inplace=True)
    df.eval('AGE_18_65 = TTL_POPULATION_ALL - AGELESS18 - AGE65PLUS', inplace=True)
    df.eval('AGE_18_65_PC = AGE_18_65 / TTL_POPULATION_ALL', inplace=True)
    df.eval('RETIRE_PC = AGE65PLUS / TTL_POPULATION_ALL', inplace=True)
    df.eval('BACH_HIGHER_PC = BACHELORS_OR_HIGHER_EDU / TTLPOP_25PLUS_EDU', inplace=True)
    df.eval('HOUSE_AFFORD = MEDIAN_HOME_VALUE / MED_HH_INCOME', inplace=True)
    df.eval('HOUSE_OWN_PC = OWNER_OCCUPIED_HU / TTL_HOUSING_UNITS', inplace=True)
    return df

if __name__ == "__main__":
    file_lst = ['2006_2010', '2010_2014', '2014_2018']
    col_lst = (['STFID','TTL_POPULATION_ALL','MALE','FEMALE','AGE_LESS_5','AGE_5_TO_9','AGE_10_TO_14', 
             'AGE_15_TO_17','AGELESS18','AGE65PLUS','AGE_20_TO_29','MEDIAN_AGE_ALL', 'MEDIAN_AGE_MALE','MEDIAN_AGE_FEMALE','TTLPOP_25PLUS_EDU', 
             'LESS_THAN_HS_DIPLOMA_EDU','HSGRAD_OR_EQUIV_EDU','SOMECOLLEGE_OR_AA_EDU','BACHELORS_OR_HIGHER_EDU', 
             'TTL_HOUSING_UNITS','OCCUPIED_HU','OWNER_OCCUPIED_HU','RENTER_OCCUPIED_HU','MED_HH_INCOME','MEDIAN_EARNINGS','MEDIAN_EARN_MALE', 
             'MEDIAN_EARN_FEMALE','MED_CONTRACT_RENT','MEDIAN_HOME_VALUE'])
    for file in file_lst:
        file_path = 'data/american_community_survey_blk_grp_'+file+'.csv'
        df = import_data(file_path, col_lst, 'STFID')
        df = calc_data(df)
        df.to_pickle('data/pickled_df_'+file)


    

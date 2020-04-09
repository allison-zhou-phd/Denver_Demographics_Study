import numpy as np
import pandas as pd
import scipy.stats as stats

if __name__ == "__main__":
    file_lst = ['2010_2014','2014_2018']
    col_interest = ['MEDIAN_AGE_ALL','HOUSE_AFFORD','MEDIAN_EARN_MALE','MEDIAN_EARN_FEMALE']

    df= pd.read_pickle('data/pickled_df_2010_2014')[col_interest]
    age_2014 = df['MEDIAN_AGE_ALL'].to_numpy()
    age_2014 = age_2014[~np.isnan(age_2014)]
    house_2014 = df['HOUSE_AFFORD'].to_numpy()
    house_2014 = house_2014[~np.isnan(house_2014)]
    gap_2014 = df.eval('MEDIAN_EARN_MALE - MEDIAN_EARN_FEMALE').to_numpy()
    gap_2014 = gap_2014[~np.isnan(gap_2014)]

    df= pd.read_pickle('data/pickled_df_2014_2018')[col_interest]
    age_2018 = df['MEDIAN_AGE_ALL'].to_numpy()
    age_2018 = age_2018[~np.isnan(age_2018)]
    house_2018 = df['HOUSE_AFFORD'].to_numpy()
    house_2018 = house_2018[~np.isnan(house_2018)]
    gap_2018 = df.eval('MEDIAN_EARN_MALE - MEDIAN_EARN_FEMALE').to_numpy()
    gap_2018 = gap_2018[~np.isnan(gap_2018)]

# Hypothesis 1: Denver's median age has NOT changed between 2010_2014 and 2014_2018. Two-tailed test, Welch' t-test
t_stat1, p_value1 = stats.ttest_ind(age_2014, age_2018, equal_var=False)
print(f"The p_value for the null hypotheis that Denver's median age has NOT changes is: {p_value1: 0.3f}")

# Hypothesis 2: Denver's housing affordability has NOT changed between 2010_2014 and 2014_2018.
t_stat2, p_value2 = stats.ttest_ind(house_2014, house_2018, equal_var=False)
print(f"The p_value for the null hypotheis that Denver's housing affordability has NOT changes is: {p_value2: 0.3f}")

# Hypothesis 3: Denver's gender pay gap has NOT changed between 2010_2014 and 2014_2018.
t_stat3, p_value3 = stats.ttest_ind(gap_2014, gap_2018, equal_var=False)
print(f"The p_value for the null hypotheis that Denver's gender pay gap has NOT changes is: {p_value3: 0.3f}")

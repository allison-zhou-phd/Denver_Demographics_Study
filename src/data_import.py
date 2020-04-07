import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':16})
plt.style.use('ggplot')

df = pd.read_csv('data/american_community_survey_blk_grp_2014_2018.csv', na_values='None')
#df = pd.read_csv('../data/american_community_survey_blk_grp_2014_2018.csv', na_values={'nan', 'None'})
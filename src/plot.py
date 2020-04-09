import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({'font.size':16})
plt.style.use('ggplot')

def plot_sideBySide_bar(df, ax, width, labels, Xticklabels, title):
    '''
        Plot multi_bar with different colors for comparison
        ARGS:
            df - pandas datafram
            ax - the axis to plot on
            width - bar width
            labels - labels for each bar chart
            Xticklabels - labels for the Xticks
            title - plot title
        Returns:
            ax - axis with plot on it
    '''
    xlocs = np.arange(len(df))
    ax.bar(xlocs-width, df.iloc[0,:], width, color='cornflowerblue', label =labels[0])
    ax.bar(xlocs, df.iloc[1,:], width, color='hotpink', label =labels[1])
    ax.bar(xlocs+width, df.iloc[2,:], width, color='red', label =labels[2])
    ax.set_xticks(ticks=range(len(df)))
    ax.set_xticklabels(Xticklabels)
    ax.yaxis.grid(True)
    ax.legend(loc='best')
    ax.set_title(title)
    return ax

if __name__ == "__main__":
    file_lst = ['2006_2010','2010_2014','2014_2018']
    n = len(file_lst)
    col_interest = ['MEDIAN_AGE_ALL','MEDIAN_AGE_MALE','MEDIAN_AGE_FEMALE','SCH_AGE','SCH_AGE_PC','AGE_18_65','AGE_18_65_PC','AGE65PLUS','RETIRE_PC',
                    'MED_HH_INCOME','MEDIAN_EARN_MALE','MEDIAN_EARN_FEMALE','HOUSE_AFFORD','HOUSE_OWN_PC']
    
    mean_lst=[]
    median_lst=[]
    house_afford=[]
    house_own=[]
    for file in file_lst:
        df = pd.read_pickle('data/pickled_df_'+file)
        df_interest = df[col_interest]
        mean_lst.append(df_interest.mean())
        median_lst.append(df_interest.median())
        house_afford.append(df_interest['HOUSE_AFFORD'])
        house_own.append(df_interest['HOUSE_OWN_PC'])
    df_mean = pd.DataFrame(data = mean_lst, columns=col_interest)
    df_median = pd.DataFrame(data = median_lst, columns=col_interest)    
    
#   Plot to mean values across 3 different timeframes in history using side-by-side bar charts
#   Age by gender
#     col_age_gender = ['MEDIAN_AGE_ALL','MEDIAN_AGE_MALE','MEDIAN_AGE_FEMALE']
#     Xtick_labels = ['All', 'Male', 'Female']
#     width = 0.2
#     fig1, ax = plt.subplots(1, 1, figsize=(8,4))
#     df_age_gender = df_mean[col_age_gender]
#     plot_sideBySide_bar(df_age_gender, ax, width, file_lst, Xtick_labels, "Mean Group Result")
#     ax.set_ylim([0,50])
#     plt.savefig('images/age_by_gender.png')

# #   Age by group
#     col_age_group = ['SCH_AGE_PC','AGE_18_65_PC','RETIRE_PC']
#     Xtick_labels = ['SchoolAge', 'WorkAge', 'RetireAge']
#     fig2, ax = plt.subplots(1, 1, figsize=(8,4))
#     df_age_group = df_mean[col_age_group]
#     plot_sideBySide_bar(df_age_group, ax, width, file_lst, Xtick_labels, "Mean Group Result")
#     plt.savefig('images/age_by_group.png')


# #   Plot stacked histograms to show the median income b/w male and female over time
#     col_inc_gender = ['MEDIAN_EARN_MALE','MEDIAN_EARN_FEMALE']
#     fig3, axs = plt.subplots(3, 1, figsize=(8,8), sharex=True)
#     for idx, ax in enumerate(axs):
#         df = pd.read_pickle('data/pickled_df_'+file_lst[idx])
#         df_inc_gender = df[col_inc_gender]
#         df_inc_gender.plot.hist(bins=30, alpha=0.7, stacked=True, ax=ax)
#         ax.axvline(df_inc_gender.median()[0], color='green')
#         ax.axvline(df_inc_gender.median()[1], color='red', label = 'Female_median')
#         ax.set_title(file_lst[idx])
#     fig3.tight_layout(pad=1)
#     plt.savefig('images/income_by_gender.png')

# #  Plot box charts to show the housing affordability over time
#     fig4, axs = plt.subplots(1, 1, figsize=(10,5))
#     df_house_afford = pd.DataFrame(data=house_afford).T
#     df_house_afford.columns = file_lst
#     ax = df_house_afford.plot.box(vert=False, fontsize='small')
#     plt.savefig('images/house_afford.png') 

#     df_house_own = pd.DataFrame(data=house_own).T
#     df_house_own.columns = file_lst
#     ax = df_house_own.plot.box(vert=False, fontsize='small')
#     plt.savefig('images/house_own.png') 

#   Focus on 2014-2018 data, use seaborn to do pairplot and study what correlates with median home value
    col_interest = ['MEDIAN_HOME_VALUE','MED_HH_INCOME','BACH_HIGHER_PC','HOUSE_OWN_PC','RETIRE_PC']
    df = pd.read_pickle('data/pickled_df_2014_2018')
    df_plot = df[col_interest]
    plt.figure(figsize=(9,9))
    sns.pairplot(df_plot, palette="husl")
    #ax.fig.suptitle("Test It", y =1.08)
    plt.show()
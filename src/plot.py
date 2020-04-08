import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':16})
plt.style.use('ggplot')

def plot_box(df, xlabel, ylabel, out_name):
    pass

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

def plot_mean_against_median(df_lst, col_interest, width, data_category, Xtick_labels, title_lst):
    fig, axs = plt.subplots(2, 1, figsize=(8,6), sharex=True)
    for idx, ax in enumerate(axs.flatten()):
        plot_sideBySide_bar(df_lst[idx][col_interest], ax, width, data_category, Xtick_labels, title_lst[idx])
    fig.tight_layout()

def plot_overlay_hist():
    pass

if __name__ == "__main__":
    file_lst = ['2006_2010','2010_2014','2014_2018']
    n = len(file_lst)
    col_interest = ['MEDIAN_AGE_ALL','MEDIAN_AGE_MALE','MEDIAN_AGE_FEMALE','SCH_AGE','SCH_AGE_PC','AGE_18_65','AGE_18_65_PC','AGE65PLUS','RETIRE_PC',
                    'MED_HH_INCOME','MEDIAN_EARN_MALE','MEDIAN_EARN_FEMALE','HOUSE_AFFORD','HOUSE_OWN_PC']
    
    mean_lst=[]
    median_lst=[]
    for file in file_lst:
        df = pd.read_pickle('data/pickled_df_'+file)
        df_interest = df[col_interest]
        mean_lst.append(df_interest.mean())
        median_lst.append(df_interest.median())
    df_mean = pd.DataFrame(data = mean_lst, columns=col_interest)
    df_median = pd.DataFrame(data = median_lst, columns=col_interest)
    df_lst =[]
    df_lst.append(df_mean)
    df_lst.append(df_median)          

    width = 0.2
#   Plot to compare the mean and median values across 3 different timeframes in history
#   Age by gender
    col_interest = ['MEDIAN_AGE_ALL','MEDIAN_AGE_MALE','MEDIAN_AGE_FEMALE']
    Xtick_labels = ['All', 'Male', 'Female']
    title_lst = ['Mean Group Result', 'Median Group Result']
    plot_mean_against_median(df_lst, col_interest, width, file_lst, Xtick_labels, title_lst)
    plt.savefig('images/age_by_gender.png')
#
    col_interest = ['SCH_AGE_PC','AGE_18_65_PC','RETIRE_PC']
    Xtick_labels = ['SchoolAge', 'WorkAge', 'RetireAge']
    title_lst = ['Mean Group Result', 'Median Group Result']
    plot_mean_against_median(df_lst, col_interest, width, file_lst, Xtick_labels, title_lst)
    plt.show()







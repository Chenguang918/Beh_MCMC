# Visualized MCMC-behavior data

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns   # seaborn 基于 matplotlib


class LoadData():  # load data

    def LoadCsvData(self, filename):
        with open(filename) as raw_data:
            data = pd.read_csv(raw_data)
        return data

class PlotViolin():

    def PlotCombinedViolin(self,data): # self 方法内的实例化调用的前提条件
        #

        sns.set(style='whitegrid', color_codes=True)
        fig, axes = plt.subplots(1, 3, figsize=(10, 5))
        sns.violinplot(x='Exp', y='Kmax', hue='tPBM', data=data, split=True, ax=axes[0], inner='box',alpha=0.5)
        sns.violinplot(x='Exp', y='Attention', hue='tPBM', data=data, split=True, ax=axes[1], inner='box',alpha=0.5)
        sns.violinplot(x='Exp', y='Guess', hue='tPBM', data=data, split=True, ax=axes[2], inner='box', alpha=0.5)
        plt.show()


#

if __name__ == '__main__':
    data1 = LoadData()  # 实例化
    plot1 = PlotViolin() #
    data=data1.LoadCsvData('C:/Users/lgh/OneDrive/Paper5/MCMC_data/Exp4_data2py.csv') # 反斜杠才对
    plot1.PlotCombinedViolin(data)

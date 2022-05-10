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
        sns.violinplot(x='Exp', y='PSI', hue='Group', data=data, split=True, inner='box',alpha=0.5)
        plt.show()


#

if __name__ == '__main__':
    data1 = LoadData()  # 实例化
    plot1 = PlotViolin() #
    data=data1.LoadCsvData('C:/Users/lgh/OneDrive/Paper5/PSI_data/PSI_data2py.csv') # 反斜杠才对
    plot1.PlotCombinedViolin(data)

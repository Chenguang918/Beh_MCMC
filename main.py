# Visualized MCMC-behavior data

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


class LoadData():

    def LoadCsvData(self, filename):
        with open(filename) as raw_data:
            data = pd.read_csv(raw_data)
        return data

class PlotViolin():

    def PlotCombinedViolin(self, xlabel, ylabel, combine_label, data): # self 方法内的实例化调用的前提条件
        #

        sns.set(style='whitegrid', color_codes=True)
        fig, axes = plt.subplots(1, 2, figsize=(10, 5))
        sns.violinplot(x=xlabel, y=ylabel, hue=combine_label, data=data, split=True, ax=axes[0], inner='point',alpha=0.5)
        plt.show()


# 按间距中的绿色按钮以运行脚本。

if __name__ == '__main__':
    data1 = LoadData()  # 实例化
    plot1 = PlotViolin()
    data=data1.LoadCsvData('C:/Users/lgh/OneDrive/Paper5/MCMC_data/text.csv') # 反斜杠才对
    plot1.PlotCombinedViolin('Exp','Kmax','tPBM',data)

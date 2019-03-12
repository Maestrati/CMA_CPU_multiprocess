#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 00:49:36 2019

@author: louismaestrati
"""


import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fig_creation(df, f, title):
    
    plt.figure(figsize=(15, 9))
    
    plt.subplot(1, 3, 1)
    plt.semilogy(df["eval"]/16, df[f])
    plt.xlabel("Iterations")
    plt.ylabel(f)
    
    plt.subplot(1, 3, 2)
    plt.semilogy(df["temps"], df[f])    
    plt.xlabel("temps")
    plt.ylabel(f)
    plt.title(title)

    plt.subplot(1, 3, 3)
    plt.plot(df["temps"], df["eval"]/16)    
    plt.xlabel("temps")
    plt.ylabel("iter")
    
    plt.show()

def plot(filepath, title):
    df = pd.read_csv(filepath, sep = ";")
    fig_creation(df, "function-value", title)
    
    
    
if __name__ == "__main__":
    
    non_para = '/Users/louismaestrati/Desktop/para_demo/res_cpu_non_para.csv'
    para = '/Users/louismaestrati/Desktop/para_demo/res_cpu_para.csv'
    
    plot(non_para, "non_para")
    plot(para, "para")
    

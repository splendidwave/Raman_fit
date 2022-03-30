import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time
from fitcures import *
from plotpic import *


def fit_para_split(g,l,v,fit_list):
    temp = []
    temp_ls = []
    fit_lower_bound = []
    fit_upper_bound = []
    for i in fit_list:
        try:
            temp = list(eval(i))
            temp_ls.append(temp)
        except SyntaxError:
            temp_ls.append(i)
        except TypeError:
            temp_ls.append(float(i))
        except:
            print('请检查拟合参数输入格式是否有误！')
    for i in range(g):
        for j in range(4):
            fit_lower_bound.append(temp_ls[j*2][i])
            fit_upper_bound.append(temp_ls[j*2+1][i])
    for i in range(l):
        for j in range(4):
            fit_lower_bound.append(temp_ls[8+j*2][i])
            fit_upper_bound.append(temp_ls[8+j*2+1][i])
    for i in range(v):
        for j in range(4):
            fit_lower_bound.append(temp_ls[16+j*2][i])
            fit_upper_bound.append(temp_ls[16+j*2+1][i])
    
    return fit_lower_bound,fit_upper_bound


def plot_now_data(x,y,g,l,v,fit_list):
    g,l,v = map(int,[g,l,v])
    fit_lower_bound,fit_upper_bound = fit_para_split(g,l,v,fit_list)
    popt,pcov = curve_fit(lambda x,temp,*p: fit_function(x,g,l,v,temp,*p),x,y,\
    bounds =(fit_lower_bound,fit_upper_bound))

    plot_fit_line(x,g,l,v,popt)
    show_the_fen(g,l,v,popt)

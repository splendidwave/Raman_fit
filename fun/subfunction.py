from scipy.optimize import curve_fit
from fitcures import *
from plotpic import *


def fit_para_split(g,l,v,fit_list):
    temp = []
    temp_ls = []
    fit_lower_bound = []
    fit_upper_bound = []
    #print(fit_list)
    for i in fit_list:
        try:
            temp = list(eval(i))    
            temp_ls.append(temp)
        except SyntaxError:
            if len(i):
                print("请检查是否输入中文逗号或有多余空格")
                return '格式','错误'
            else:
                temp_ls.append(i)
        except TypeError:
            temp_ls.append([float(i)])
        except:
            print('请检查拟合参数输入格式是否有误！')
    #print(temp_ls)
    try:
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
    except IndexError:
        print("请检查输入参数是否格式错误")
        return '格式','错误'
    if len(fit_lower_bound) != len(fit_upper_bound):
        print("请检查是否存在遗漏参数")
        return '格式','错误'
    return fit_lower_bound,fit_upper_bound


def plot_now_data(x,y,g,l,v,fit_list,sub = True, style = style):
    g,l,v = map(int,[g,l,v])
    fit_lower_bound,fit_upper_bound = fit_para_split(g,l,v,fit_list)
    if fit_lower_bound == "格式":
        print('拟合失败')
    else:
        try:
            popt,pcov = curve_fit(lambda x,temp,*p: fit_function(x,g,l,v,temp,*p),x,y,\
            bounds =(fit_lower_bound,fit_upper_bound))

            plot_fit_line(x,g,l,v,popt,sub = sub, style = style)
            show_the_fen(g,l,v,popt)
            return [popt,g,l,v]
        except RuntimeError:
            print('拟合超时,请检查参数设置是否合理')
            
def plot_overview(x,popt_list,sub,style):
    temp = 0
    for i in range(len(popt_list)):
        popt_c = popt_list[i][0].copy()
        popt_c[0] += temp 
        temp += plot_fit_line(x,popt_list[i][1],popt_list[i][2],popt_list[i][3],popt_c,\
            sub = sub, style = style, number = i)

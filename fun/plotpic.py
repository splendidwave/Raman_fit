import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import MultipleLocator
from fitcures import *
from setting import *


def plot_scatter(x,st):
    plt.scatter(x, st, alpha=0.8,s=13,color=scatter_color)

def show_the_fen(g,l,v,popt):
    #y01,a1,p1,f1,y02,a2,p2,f2,y03,a3,xc3,w3,y04,a4,xc4,w4 = popt
    form = "{:10}\t{:10}\t{:10}\t{:10}\t{:10}"
    print("拟合成功！")
    print("拟合参数如下：")
    print(form.format("峰类型","偏置","幅值","中心位置","宽度"))
    for i in range(g):
        print(form.format("Gauss","%.2f"%popt[i*4],"%.2f"%popt[i*4+1],"%.2f"%popt[i*4+2],"%.2f"%popt[i*4+3]))
    for i in range(g,g+l):
        print(form.format("Gauss","%.2f"%popt[i*4],"%.2f"%popt[i*4+1],"%.2f"%popt[i*4+2],"%.2f"%popt[i*4+3]))
    for i in range(g+l,g+l+v):
        print(form.format("Voigt","%.2f"%popt[i*4],"%.2f"%popt[i*4+1],"%.2f"%popt[i*4+2],"%.2f"%popt[i*4+3]))



    

# 拟合曲线绘制
def plot_fit_line(x,g,l,v,popt,sub = True):
    xfit = np.linspace(x.min(),x.max(),5000)
    yfit = fit_function(xfit,g,l,v,'',popt)
    plt.plot(xfit,yfit,linewidth=fit_line_width,color = fit_line_color)
    # 绘制分峰
    if sub:
        y00 = 0
        for i in range(g+l+v):
            y00 += popt[i*4]
        for i in range(g):
            yfit2 = Gauss(xfit,y00,popt[i*4+1],popt[i*4+2],popt[i*4+3])
            plt.plot(xfit,yfit2,linewidth=fit_subline_width[0][i%len(fit_subline_width[0])],\
                     linestyle=fit_subline_style[0][i%len(fit_subline_style[0])],\
                     color=fit_subline_color[0][i%len(fit_subline_color[0])])
        for i in range(g,g+l):
            yfit3 = Lorentz(xfit,y00,popt[i*4+1],popt[i*4+2],popt[i*4+3])
            plt.plot(xfit,yfit3,linewidth=fit_subline_width[1][i%len(fit_subline_width[1])],\
                     linestyle=fit_subline_style[1][i%len(fit_subline_style[1])],\
                     color=fit_subline_color[1][i%len(fit_subline_color[1])])
        for i in range(g+l,g+l+v):
            yfit4 = Voigt(xfit,y00,popt[i*4+1],popt[i*4+2],popt[i*4+3])
            plt.plot(xfit,yfit4,linewidth=fit_subline_width[2][i%len(fit_subline_width[2])],\
                     linestyle=fit_subline_style[2][i%len(fit_subline_style[2])],\
                     color=fit_subline_color[2][i%len(fit_subline_color[2])])


def ready_to_show():
    x_major_locator=MultipleLocator(10)#准备刻度
    #标签
    plt.xlabel('wavenumber',fontdict={'family' : 'Times New Roman', 'size'   : 29})
    plt.ylabel('intensity(arb.units)',fontdict={'family' : 'Times New Roman', 'size'   : 29})
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)         #画刻度
    plt.xlim(0,120)
    plt.grid(axis='x',linestyle='-.')                   #画竖线
    #plt.text(100,80,'atm',ha = 'center',va = 'bottom',fontsize=7)#加标签
    #ax.set_yticks([])#隐藏y轴刻度
    plt.yticks(fontproperties = 'Times New Roman', size = 23)
    plt.xticks(fontproperties = 'Times New Roman', size = 23)
    plt.show()                         #展示




import numpy as np
from scipy.special import wofz

def Lorentz(x,y0,A,xc,w):
    y = y0 + w*A*(w/(4*(x-xc)**2 + w**2))
    return y

def Gauss(x,y0,A,xc,w):
    y = y0 + A * np.exp(-2*((x-xc)/w)**2)
    return y

def Voigt(x, y0, amp, pos, fwhm, shape = 1):
    tmp = 1/wofz(np.zeros((len(x))) + 1j*np.sqrt(np.log(2.0))*shape).real
    return y0+tmp*amp*wofz(2*np.sqrt(np.log(2.0))*(x-pos)/fwhm+1j*np.sqrt(np.log(2.0))*shape).real

# 多峰拟合函数
# g,l,v分别为高斯、洛伦兹和Voigt峰的数量
# temp和p是参数，每个峰有4个参数
def fit_function(x,g,l,v,temp,*p):
    y = 0
    if isinstance(temp,str):
        p = list(p[0])
    else:
        p = list(p)
        p.insert(0,temp)
    for i in range(g):
        y += Gauss(x,p[i*4+0],p[i*4+1],p[i*4+2],p[i*4+3])
    for i in range(g,g+l):
        y += Lorentz(x,p[i*4+0],p[i*4+1],p[i*4+2],p[i*4+3])
    for i in range(g+l,g+l+v):
        y += Voigt(x,p[i*4+0],p[i*4+1],p[i*4+2],p[i*4+3])
    return y


def lc_mode_sub(x,a,c):
    y = a*np.sqrt(1 - np.cos(np.pi/x))+c
    return y

def lc_mode_plus(x,a,c):
    y = a*np.sqrt(1 + np.cos(np.pi/x))+c
    return y

import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from fitcures import *
from plotpic import *
from subfunction import *


class verification_window(tk.Frame):

    # 调用时初始化
    def __init__(self):
        global root
        root = tk.Tk()
        root.resizable(width=False, height=False)
        try:
            root.iconbitmap(default = 'Rs.ico')
        except:
            print("未成功加载图标")
        root.title("拉曼拟合2.1")
        root.geometry('580x850')
        super().__init__()
        self.filename = tk.StringVar()  # 文件名
        self.df = pd.DataFrame()        # 数据块
        self.popt = []                  # 参数记录
        self.popt_list = []             # 绘制总览数据
        self.help_count = 0             # 帮助手册序号
        self.pack()
        self.init_data()
        self.main_window()
        root.mainloop()

    # 窗口布局
    def main_window(self):
        global root
        # 抬头
        info_label = tk.Label(root,text='请按照提示输入参数:',font=('宋体',20)).place(x=40, y=10)

        # 文件名行
        filename_label = tk.Label(root,text='1.文件名:',font=('宋体',12)).place(x=50, y=70)
        filename_entry = tk.Entry(root,textvariable=self.filename).place(x=180, y = 70)
        # 选择文件按钮
        choose_button = tk.Button(root, text='选择文件', command=self.choosefile, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        choose_button.place(x=400,y=65)

        # 高斯峰数量选择
        Gauss_number_bar_label = tk.Label(root,text='2.选择 Gauss 峰数量:',font=('宋体',12)).place(x=50, y=120)
        Gauss_number_bar = tk.Scale(root,from_=0,to=10,orient=tk.HORIZONTAL,length=200,showvalue=1,tickinterval=3,resolution=1,command=self.choose_Gauss_number)
        Gauss_number_bar.place(x = 300, y = 100)
        Gauss_number_bar.set(self.Gauss_number)

        # 洛伦兹峰数量选择
        Lorentz_number_bar_label = tk.Label(root,text='3.选择 Lorentz 峰数量:',font=('宋体',12)).place(x=50, y=220)
        Lorentz_number_bar = tk.Scale(root,from_=0,to=10,orient=tk.HORIZONTAL,length=200,showvalue=1,tickinterval=3,resolution=1,command=self.choose_Lorentz_number)
        Lorentz_number_bar.place(x = 300, y = 200)
        Lorentz_number_bar.set(self.Lorentz_number)

        # voigt峰数量选择
        Voigt_number_bar_label = tk.Label(root,text='4.选择 Voigt 峰数量:',font=('宋体',12)).place(x=50, y=320)
        Voigt_number_bar = tk.Scale(root,from_=0,to=10,orient=tk.HORIZONTAL,length=200,showvalue=1,tickinterval=3,resolution=1,command=self.choose_Voigt_number)
        Voigt_number_bar.place(x = 300, y = 300)
        Voigt_number_bar.set(self.Voigt_number)

        # 波数选择
        Wave_number_bar_label = tk.Label(root,text='5.选择波数所在列:',font=('宋体',12)).place(x=50, y=400)
        Wave_number_bar = tk.Scale(root,from_= 0,to=20,orient=tk.HORIZONTAL,length=450,showvalue=1,tickinterval=3,resolution=1,command=self.choose_Wave_number)
        Wave_number_bar.place(x = 50, y = 430)
        Wave_number_bar.set(self.Wave_number)
        
        # 波数选择
        Now_data_bar_label = tk.Label(root,text='6.选择待处理数据列:',font=('宋体',12)).place(x=50, y=530)
        Now_data_bar = tk.Scale(root,from_= 0,to=20,orient=tk.HORIZONTAL,length=450,showvalue=1,tickinterval=3,resolution=1,command=self.choose_Now_data)
        Now_data_bar.place(x = 50, y = 560)
        Now_data_bar.set(self.Now_data)
        
        # 载入参数按钮
        return_button = tk.Button(root, text='载入参数', command=self.turn_back, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        return_button.place(x=40,y=700)
        # 拟合峰参数按钮
        load_button = tk.Button(root, text='拟合峰参数', command=self.minibox1, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        load_button.place(x=170,y=700)
        # 绘图参数按钮
        dai_button = tk.Button(root, text='绘图参数', command=self.minibox2, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        dai_button.place(x=300,y=700)
        # 保存按钮
        save_button = tk.Button(root, text='保存参数', command=self.save, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        save_button.place(x=430,y=700)
        # 查看当前数据按钮
        scatter_button = tk.Button(root, text='查看数据', command=self.load_data, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        scatter_button.place(x=40,y=750)
        # 拟合当前按钮
        single_button = tk.Button(root, text='拟合', command=self.fit_now_data, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        single_button.place(x=170,y=750)
        # 记录拟合按钮
        setting_button = tk.Button(root, text='记录', command=self.record, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        setting_button.place(x=300,y=750)
        # 绘制所有按钮
        all_button = tk.Button(root, text='绘制总览', command=self.overview, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        all_button.place(x=430,y=750)
        # 退出按钮
        quit_button = tk.Button(root, text='退出', command=self.quit, fg='white', bg='black', activeforeground='white', activebackground='red', width=10, height=1)
        quit_button.place(x=460,y=800)
        # 帮助文档
        help_button = tk.Button(root, text='帮助', command=self.help, fg='white', bg='black', activeforeground='white', activebackground='green', width=10, height=1)
        help_button.place(x=20,y=800)

    # 选择文件按键
    def choosefile(self):
        filepath = tk.filedialog.askopenfilename(title=u'选择文件')
        self.filename.set(filepath[:-4])
        self.main_window()

    # 改变三个峰的条
    def choose_Gauss_number(self,V):
        self.Gauss_number = V
    def choose_Lorentz_number(self,V):
        self.Lorentz_number = V
    def choose_Voigt_number(self,V):
        self.Voigt_number = V

    # 改变选中的数据
    def choose_Wave_number(self,V):
        self.Wave_number = V
    def choose_Now_data(self,V):
        self.Now_data = V
    
    # 查看数据函数
    def load_data(self):
        filename = self.filename.get()+'.csv'
        try:
            self.df = pd.read_csv(filename)
            print("载入成功")
            print('文件共有%d列\n'%self.df.shape[1])
            print("文件前5行如下：")
            print(self.df.head())
            print()
            print("正在尝试绘制散点图.....")
            x = self.df.iloc[:,int(self.Wave_number)].values
            y = self.df.iloc[:,int(self.Now_data)].values
            plt.figure(1)
            plot_scatter(x,y,scatter_size = self.scatter[1], scatter_color = self.scatter[0])
            print('绘制成功\n')
            ready_to_show(x,x_label = self.label[0] ,y_label = self.label[1])
        except FileNotFoundError:
            print("未找到对应文件\n")
                
     
    # 载入文件参数
    def turn_back(self):
        file_path = tk.filedialog.askopenfilename(title=u'选择要读取的文件')
        if file_path[-4:] != '.npz':
            messagebox.showinfo(title='提示', message='请选择.pnz后缀的文件')
        else:
            self.init_data(filename = file_path)
            self.main_window()
        
    def init_data(self, filename = 'last.npz'):
        try:
            # 读取文件数据
            last_data = np.load(filename)
            # 读取主界面参数设定
            main_setting = last_data['arr_0']
            self.filename.set(main_setting[0])
            self.Gauss_number, self.Lorentz_number, self.Voigt_number,self.Wave_number, self.Now_data = main_setting[1:]
            # 读取拟合峰参数设定
            temp = last_data['arr_1']
            self.fit_list = ['' for i in range(24)] #峰的参数
            self.fit_list_var = [tk.StringVar() for i in range(24)]
            for i in range(24):
                self.fit_list_var[i].set(temp[i])
                self.fit_list[i] = str(temp[i])
            # 读取画图参数设定
            temp = last_data['arr_2']
            self.label = eval(temp[0])
            self.scatter = eval(temp[1])
            self.sub = eval(temp[2])
            self.style = eval(temp[3])
            self.setting_var = [tk.StringVar() for i in range(15)]  # 设置参数框
            self.sub_var = tk.StringVar()           #设置选框
            self.sub_var.set(str(self.sub))
            # 赋值
            self.setting_var[0].set(str(self.label[0]))
            self.setting_var[1].set(str(self.label[1]))
            self.setting_var[2].set(str(self.scatter[0]))
            self.setting_var[3].set(str(self.scatter[1]))
            for i in range(2):
                self.setting_var[4+i].set(str(self.style[i]))
            for i in range(3):
                self.setting_var[6+i].set(str(self.style[2][i]))
                self.setting_var[9+i].set(str(self.style[3][i]))
                self.setting_var[12+i].set(str(self.style[4][i]))
        except:
            self.filename.set('demo')
            self.Gauss_number = 1        # 高斯峰数量
            self.Lorentz_number = 0      # 洛伦兹峰数量
            self.Voigt_number = 0        # voigt峰数量
            self.Wave_number = 0         # 波数的位置
            self.Now_data = 1            # 当前数据列
            self.fit_list = ['' for i in range(24)] #峰的参数
            self.fit_list_var = [tk.StringVar() for i in range(24)] # 拟合参数框
            for i in range(24):
                self.fit_list_var[i].set(self.fit_list[i])
            # 读取画图参数设定
            self.setting_var = [tk.StringVar() for i in range(15)]  # 设置参数框
            self.sub_var = tk.StringVar()           #设置选框
            self.sub_var.set('True')
            self.sub = True                     #设置子峰
            self.style = style
            self.label = ['wavenumber','intensity(arb.units)'] # xy标签
            self.setting_var[0].set(str(self.label[0]))
            self.setting_var[1].set(str(self.label[1]))
            self.scatter = [scatter_color,scatter_size]        # 散点参数
            self.setting_var[2].set(str(self.scatter[0]))
            self.setting_var[3].set(str(self.scatter[1]))
            for i in range(2):
                self.setting_var[4+i].set(str(self.style[i]))
            for i in range(3):
                self.setting_var[6+i].set(str(self.style[2][i]))
                self.setting_var[9+i].set(str(self.style[3][i]))
                self.setting_var[12+i].set(str(self.style[4][i]))

    # 设置拟合峰参数 !！子窗口
    def minibox1(self):
        global top_box
        top_box = tk.Toplevel()
        top_box.resizable(width=False, height=False)
        top_box.title("拟合峰参数")
        top_box.geometry('1200x680')
        info_label2 = tk.Label(top_box,text='请设置详细参数,多个数据使用英文逗号分隔:',font=('宋体',20)).place(x=40, y=10)

        # 高斯峰信息记录
        info_label5 = tk.Label(top_box,text="Gauss峰数量为: {}".format(self.Gauss_number),font=('宋体',12)).place(x=40, y=120)
        offset_min_label = tk.Label(top_box,text='偏置最小值(y0):',font=('宋体',10)).place(x=250, y=70)
        offset_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[0]).place(x=420, y=70)
        offset_max_label = tk.Label(top_box,text='偏置最大值(y0):',font=('宋体',10)).place(x=250, y=100)
        offset_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[1]).place(x=420, y=100)
        amplitude_min_label = tk.Label(top_box,text='幅值最小值(A):',font=('宋体',10)).place(x=250, y=140)
        amplitude_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[2]).place(x=420, y=140)
        amplitude_max_label = tk.Label(top_box,text='幅值最大值(A):',font=('宋体',10)).place(x=250, y=170)
        amplitude_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[3]).place(x=420, y=170)
        
        center_min_label = tk.Label(top_box,text='中心位置最小值(c):',font=('宋体',10)).place(x=660, y=70)
        center_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[4]).place(x=840, y=70)
        center_max_label = tk.Label(top_box,text='中心位置最大值(c):',font=('宋体',10)).place(x=660, y=100)
        center_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[5]).place(x=840, y=100)
        width_min_label = tk.Label(top_box,text='宽度最小值(w):',font=('宋体',10)).place(x=660, y=140)
        width_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[6]).place(x=840, y=140)
        width_max_label = tk.Label(top_box,text='宽度最大值(w):',font=('宋体',10)).place(x=660, y=170)
        width_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[7]).place(x=840, y=170)

        # 洛伦兹峰信息记录
        info_label6 = tk.Label(top_box,text="Lorentz峰数量为: {}".format(self.Lorentz_number),font=('宋体',12)).place(x=40, y=300)
        offset_min_label = tk.Label(top_box,text='偏置最小值(y0):',font=('宋体',10)).place(x=250, y=250)
        offset_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[8]).place(x=420, y=250)
        offset_max_label = tk.Label(top_box,text='偏置最大值(y0):',font=('宋体',10)).place(x=250, y=280)
        offset_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[9]).place(x=420, y=280)
        amplitude_min_label = tk.Label(top_box,text='幅值最小值(A):',font=('宋体',10)).place(x=250, y=320)
        amplitude_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[10]).place(x=420, y=320)
        amplitude_max_label = tk.Label(top_box,text='幅值最大值(A):',font=('宋体',10)).place(x=250, y=350)
        amplitude_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[11]).place(x=420, y=350)
        
        center_min_label = tk.Label(top_box,text='中心位置最小值(c):',font=('宋体',10)).place(x=660, y=250)
        center_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[12]).place(x=840, y=250)
        center_max_label = tk.Label(top_box,text='中心位置最大值(c):',font=('宋体',10)).place(x=660, y=280)
        center_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[13]).place(x=840, y=280)
        width_min_label = tk.Label(top_box,text='宽度最小值(w):',font=('宋体',10)).place(x=660, y=320)
        width_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[14]).place(x=840, y=320)
        width_max_label = tk.Label(top_box,text='宽度最大值(w):',font=('宋体',10)).place(x=660, y=350)
        width_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[15]).place(x=840, y=350)


        # voigt峰信息记录
        info_label7 = tk.Label(top_box,text="Voigt峰数量为: {}".format(self.Voigt_number),font=('宋体',12)).place(x=40, y=480)
        offset_min_label = tk.Label(top_box,text='偏置最小值(y0):',font=('宋体',10)).place(x=250, y=430)
        offset_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[16]).place(x=420, y=430)
        offset_max_label = tk.Label(top_box,text='偏置最大值(y0):',font=('宋体',10)).place(x=250, y=460)
        offset_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[17]).place(x=420, y=460)
        amplitude_min_label = tk.Label(top_box,text='幅值最小值(A):',font=('宋体',10)).place(x=250, y=500)
        amplitude_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[18]).place(x=420, y=500)
        amplitude_max_label = tk.Label(top_box,text='幅值最大值(A):',font=('宋体',10)).place(x=250, y=530)
        amplitude_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[19]).place(x=420, y=530)
        
        center_min_label = tk.Label(top_box,text='中心位置最小值(c):',font=('宋体',10)).place(x=660, y=430)
        center_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[20]).place(x=840, y=430)
        center_max_label = tk.Label(top_box,text='中心位置最大值(c):',font=('宋体',10)).place(x=660, y=460)
        center_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[21]).place(x=840, y=460)
        width_min_label = tk.Label(top_box,text='宽度最小值(w):',font=('宋体',10)).place(x=660, y=500)
        width_min_entry = tk.Entry(top_box,textvariable=self.fit_list_var[22]).place(x=840, y=500)
        width_max_label = tk.Label(top_box,text='宽度最大值(w):',font=('宋体',10)).place(x=660, y=530)
        width_max_entry = tk.Entry(top_box,textvariable=self.fit_list_var[23]).place(x=840, y=530)
        
        # 确认按钮
        confirm_button = tk.Button(top_box, text='确认', command=self.confirm, fg='white', bg='black', activeforeground='white', activebackground='red', width=10, height=1)
        confirm_button.place(x=1000,y=630)
        # 帮助文档
        help_button2 = tk.Button(top_box, text='帮助', command=self.help2, fg='white', bg='black', activeforeground='white', activebackground='green', width=10, height=1)
        help_button2.place(x=850,y=630)
        
    def minibox2(self):
        global top_box2
        top_box2 = tk.Toplevel()
        top_box2.title("绘图参数设置")
        top_box2.geometry('1200x680')
        top_box2.resizable(width=False, height=False)
        #info_label8 = tk.Label(top_box2,text='此功能正在未开发！',font=('宋体',20)).place(x=40, y=10)
        # xy标签
        tk.Label(top_box2,text='x轴标签:',font=('宋体',10)).place(x=100, y=10)
        tk.Entry(top_box2,textvariable=self.setting_var[0]).place(x=50, y=35)
        tk.Label(top_box2,text='y轴标签:',font=('宋体',10)).place(x=400, y=10)
        tk.Entry(top_box2,textvariable=self.setting_var[1]).place(x=350, y=35)

        # 散点设置
        tk.Label(top_box2,text='散点颜色:',font=('宋体',10)).place(x=700, y=10)
        tk.Entry(top_box2,textvariable=self.setting_var[2]).place(x=650, y=35)
        tk.Label(top_box2,text='散点大小:',font=('宋体',10)).place(x=1000, y=10)
        tk.Entry(top_box2,textvariable=self.setting_var[3]).place(x=950, y=35)

        # 峰设置参数
        # 标签
        tk.Label(top_box2,text='主拟合线',font=('宋体',18)).place(x=50, y=200)
        tk.Label(top_box2,text='子\n峰',font=('宋体',18)).place(x=50, y=390)
        tk.Label(top_box2,text='Gauss峰:',font=('宋体',12)).place(x=110, y=300)
        tk.Label(top_box2,text='Lorentz峰:',font=('宋体',12)).place(x=100, y=400)
        tk.Label(top_box2,text='Voigt峰:',font=('宋体',12)).place(x=110, y=500)
        tk.Label(top_box2,text='粗细',font=('宋体',16)).place(x=400, y=120)
        tk.Label(top_box2,text='颜色',font=('宋体',16)).place(x=700, y=120)
        tk.Label(top_box2,text='线型',font=('宋体',16)).place(x=1000, y=120)
        # 输入框
        tk.Entry(top_box2,textvariable=self.setting_var[4]).place(x=350, y=210)
        tk.Entry(top_box2,textvariable=self.setting_var[5]).place(x=650, y=210)
        
        tk.Entry(top_box2,textvariable=self.setting_var[6]).place(x=350, y=300)
        tk.Entry(top_box2,textvariable=self.setting_var[9]).place(x=650, y=300)
        tk.Entry(top_box2,textvariable=self.setting_var[12]).place(x=950, y=300)

        tk.Entry(top_box2,textvariable=self.setting_var[7]).place(x=350, y=400)
        tk.Entry(top_box2,textvariable=self.setting_var[10]).place(x=650, y=400)
        tk.Entry(top_box2,textvariable=self.setting_var[13]).place(x=950, y=400)

        tk.Entry(top_box2,textvariable=self.setting_var[8]).place(x=350, y=500)
        tk.Entry(top_box2,textvariable=self.setting_var[11]).place(x=650, y=500)
        tk.Entry(top_box2,textvariable=self.setting_var[14]).place(x=950, y=500)

        # 子峰
        C1 = tk.Checkbutton(top_box2,variable = self.sub_var, \
                onvalue = 'True', offvalue = 'False').place(x=10,y=410)

        # 确认按钮
        confirm_button2 = tk.Button(top_box2, text='确认', command=self.confirm2, fg='white', bg='black', activeforeground='white', activebackground='red', width=10, height=1)
        confirm_button2.place(x=1000,y=630)
        # 帮助文档
        help_button3 = tk.Button(top_box2, text='帮助', command=self.help3, fg='white', bg='black', activeforeground='white', activebackground='green', width=10, height=1)
        help_button3.place(x=850,y=630)
        

        
    # 拟合当前
    def fit_now_data(self):
        print()
        try:
            print("正在尝试拟合....")
            filename = self.filename.get()+'.csv'
            self.df = pd.read_csv(filename)
            x = self.df.iloc[:,int(self.Wave_number)].values
            y = self.df.iloc[:,int(self.Now_data)].values
            plt.figure(2)
            plot_scatter(x,y,scatter_size = self.scatter[1], scatter_color = self.scatter[0])
            self.popt = plot_now_data(x,y,self.Gauss_number, self.Lorentz_number, self.Voigt_number,self.fit_list,\
                sub = self.sub, style = self.style)
            ready_to_show(x,x_label = self.label[0] ,y_label = self.label[1])
        except FileNotFoundError:
            print("未找到对应文件\n")
            
    # 记录本次拟合
    def record(self):
        if len(self.popt):
            self.popt_list.append(self.popt)
            messagebox.showinfo(title='提醒', message='记录成功')
            self.popt = []
        else:
            messagebox.showinfo(title='提醒', message='参数已记录或拟合未完成，请再次拟合吧')
        #print(self.popt_list)

    # 绘制总览
    def overview(self):
        if len(self.popt_list) == 0:
            messagebox.showinfo(title='提醒', message='至少先记录一次数据吧(*_*)')
        else:
            print("正在尝试绘制....")
            filename = self.filename.get()+'.csv'
            self.df = pd.read_csv(filename)
            x = self.df.iloc[:,int(self.Wave_number)].values
            plt.figure(3)
            plot_overview(x,self.popt_list,sub = self.sub, style = self.style)
            ready_to_show(x,x_label = self.label[0] ,y_label = self.label[1])
            
    # 帮助文档
    def help(self):
        if self.help_count == 0:
            messagebox.showinfo(title='帮助', message='0.多次点击本按钮会给不同的提示')
            self.help_count += 1
        elif self.help_count == 1:
            messagebox.showinfo(title='帮助', message='1.在demo中可以尝试随意点击按钮')
            self.help_count += 1
        elif self.help_count == 2:
            messagebox.showinfo(title='帮助', message='2.数据文件要求UTF-8格式保存的CSV文件')
            self.help_count += 1
        elif self.help_count == 3:
            messagebox.showinfo(title='帮助', message='3.文件名在最上面的输入框输入，不需要输入后缀')
            self.help_count += 1
        elif self.help_count == 4:
            messagebox.showinfo(title='帮助', message='4.多次点击记录就可以使用绘制总览查看合图')
            self.help_count = 0
            
    # 帮助文档2--拟合峰的详细参数设定
    def help2(self):
        print("该窗口左侧显示3个峰的数量。")
        print("注意参数不要超出该数目。\n")
        print("每个峰会有4个参数（偏置，幅值，中心位置，半高宽）\n\
在该窗口可以设置每个峰的拟合范围（最大值和最小值）\n")
        print("您可以先通过点击“查看数据”\
按钮大致观察峰存在的范围然后依次输入。\n")
        print("如果拟合曲线有多个相同峰，如4个高斯峰，\n\
则在Gauss输入框中按顺序写下4个峰的参数，中间用英文逗号分隔。\n")
        messagebox.showinfo(title='帮助', message='看控制台(￣▽￣)')
        
    # 帮助文档3--绘图的详细参数设定
    def help3(self):
        messagebox.showinfo(title='help', message='按python格式输入，用列表')
        
    # 退出
    def quit(self):
        global root
        if messagebox.askquestion(title='退出', message='是否记录本次参数'):
            save_name = 'last.npz'
            save_list = [self.filename.get(), self.Gauss_number, self.Lorentz_number, self.Voigt_number, self.Wave_number, self.Now_data]
            save_setting = [str(self.label),str(self.scatter),str(self.sub),str(self.style)]
            np.savez(save_name, save_list, self.fit_list, save_setting)
        root.destroy()
        
    # 保存参数
    def save(self):
        save_name = tk.filedialog.asksaveasfilename(title=u'保存参数')
        if save_name == '':
            messagebox.showinfo(title='提示', message='未保存成功')
            return 0
        if save_name[-4:] != '.npz': 
            save_name += '.npz'
        save_list = [self.filename.get(), self.Gauss_number, self.Lorentz_number, self.Voigt_number, self.Wave_number, self.Now_data]
        save_setting = [str(self.label),str(self.scatter),str(self.sub),str(self.style)]
        np.savez(save_name, save_list, self.fit_list, save_setting)
        messagebox.showinfo(title='提示', message='保存成功')
    
    #退出子窗口1
    def confirm(self):
        global top_box
        for i in range(24):
            self.fit_list[i] = self.fit_list_var[i].get()
        top_box.destroy()
        
    #退出子窗口2
    def confirm2(self):
        global top_box2
        self.label = [self.setting_var[0].get(),self.setting_var[1].get()]
        self.scatter = [self.setting_var[2].get(),eval(self.setting_var[3].get())]
        self.style[0] = eval(self.setting_var[4].get())
        self.style[1] = eval(self.setting_var[5].get())
        self.style[2] = [eval(self.setting_var[6].get()),eval(self.setting_var[7].get()),eval(self.setting_var[8].get())]
        self.style[3] = [eval(self.setting_var[9].get()),eval(self.setting_var[10].get()),eval(self.setting_var[11].get())]
        self.style[4] = [eval(self.setting_var[12].get()),eval(self.setting_var[13].get()),eval(self.setting_var[14].get())]
        self.sub = eval(self.sub_var.get())
        top_box2.destroy()

        
if __name__ == '__main__':
    input_para = verification_window()
    

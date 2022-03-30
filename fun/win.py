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
        root.iconbitmap(default = 'Rs.ico')
        root.title("拉曼拟合1.0")
        root.geometry('580x850')
        super().__init__()
        self.filename = tk.StringVar()  # 文件名
        self.df = pd.DataFrame()        # 数据块
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
        
        # 读取参数文件按钮
        return_button = tk.Button(root, text='读取参数文件', command=self.turn_back, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        return_button.place(x=40,y=700)
        # 拟合峰参数按钮
        load_button = tk.Button(root, text='拟合峰参数', command=self.minibox1, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        load_button.place(x=170,y=700)
        # 绘图参数按钮
        dai_button = tk.Button(root, text='绘图参数', command=self.minibox2, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        dai_button.place(x=300,y=700)
        # 保存按钮
        save_button = tk.Button(root, text='保存当前参数', command=self.save, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        save_button.place(x=430,y=700)
        # 载入文件数据按钮
        scatter_button = tk.Button(root, text='载入文件数据', command=self.load_data, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        scatter_button.place(x=40,y=750)
        # 绘制散点图按钮
        single_button = tk.Button(root, text='绘制散点图', command=self.plot_statter, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        single_button.place(x=170,y=750)
        # 拟合当前按钮
        setting_button = tk.Button(root, text='拟合当前', command=self.fit_now_data, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        setting_button.place(x=300,y=750)
        # 绘制所有按钮
        all_button = tk.Button(root, text='绘制总览图', command=self.help, fg='black', bg='white', activeforeground='white', activebackground='black', width=10, height=1)
        all_button.place(x=430,y=750)
        # 退出按钮
        quit_button = tk.Button(root, text='退出', command=self.quit, fg='white', bg='black', activeforeground='white', activebackground='red', width=10, height=1)
        quit_button.place(x=460,y=800)
        # 帮助文档
        help_button = tk.Button(root, text='帮助', command=self.help, fg='white', bg='black', activeforeground='white', activebackground='green', width=10, height=1)
        help_button.place(x=20,y=800)

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
    
    # 载入数据函数
    def load_data(self):
        filename = self.filename.get()+'.csv'
        try:
            self.df = pd.read_csv(filename)
            print("载入成功")
            print("文件前5行如下：")
            print(self.df.head())
        except FileNotFoundError:
            print("未找到对应文件\n")
                
     
    # 回复上次设定
    def turn_back(self):
        file_path = tk.filedialog.askopenfilename(title=u'选择要读取的文件')
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
        except:
            self.filename.set('筛选后的数据')
            self.Gauss_number = 1        # 高斯峰数量
            self.Lorentz_number = 0      # 洛伦兹峰数量
            self.Voigt_number = 0        # voigt峰数量
            self.Wave_number = 0         # 波数的位置
            self.Now_data = 1            # 当前数据列
            self.fit_list = ['' for i in range(24)] #峰的参数
            self.fit_list_var = [tk.StringVar() for i in range(24)]
            for i in range(24):
                self.fit_list_var[i].set(self.fit_list[i])
                

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
        info_label8 = tk.Label(top_box2,text='此功能尚未开发！可以在setting.py文件中进行修改',font=('宋体',20)).place(x=40, y=10)
        
        # 确认按钮
        confirm_button2 = tk.Button(top_box2, text='确认', command=self.confirm2, fg='white', bg='black', activeforeground='white', activebackground='red', width=10, height=1)
        confirm_button2.place(x=1000,y=630)
        # 帮助文档
        help_button3 = tk.Button(top_box2, text='帮助', command=self.help3, fg='white', bg='black', activeforeground='white', activebackground='green', width=10, height=1)
        help_button3.place(x=850,y=630)
        
    # 绘制散点图
    def plot_statter(self):
        print()
        try:
            print("正在尝试绘制散点图.....")
            filename = self.filename.get()+'.csv'
            self.df = pd.read_csv(filename)
            x = self.df.iloc[:,int(self.Wave_number)].values
            y = self.df.iloc[:,int(self.Now_data)].values
            plt.figure(1)
            plot_scatter(x,y)
            print('绘制成功\n')
            ready_to_show()
        except FileNotFoundError:
            print("未找到对应文件\n")
        
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
            plot_scatter(x,y)
            plot_now_data(x,y,self.Gauss_number, self.Lorentz_number, self.Voigt_number,self.fit_list)
            ready_to_show()
        except FileNotFoundError:
            print("未找到对应文件\n")
        
    # 帮助文档
    def help(self):
        messagebox.showinfo(title='help', message='哈哈，你被骗了！我并不能给你帮助')
        

    # 帮助文档2--拟合峰的详细参数设定
    def help2(self):
        #messagebox.showinfo(title='help', message='现在啥也没有')
        print("该窗口左侧显示3个峰的数量。")
        print("注意参数不要超出该数目。\n")
        print("每个峰会有4个参数（偏置，幅值，中心位置，半高宽）\n\
在该窗口可以设置每个峰的拟合范围（最大值和最小值）\n")
        print("您可以先通过点击“绘制散点图”\
按钮大致观察峰存在的范围然后依次输入。\n")
        print("如果拟合曲线有多个相同峰，如4个高斯峰，\n\
则在Gauss输入框中按顺序写下4个峰的参数，中间用英文逗号分割。\n")
        
    # 帮助文档3--绘图的详细参数设定
    def help3(self):
        messagebox.showinfo(title='help', message='现在啥也没有')
        
    # 退出
    def quit(self):
        global root
        if messagebox.askquestion(title='退出', message='是否记录本次参数'):
            save_name = 'last.npz'
            save_list = [self.filename.get(), self.Gauss_number, self.Lorentz_number, self.Voigt_number, self.Wave_number, self.Now_data]
            np.savez(save_name, save_list, self.fit_list)
        root.destroy()
        
    # 保存参数
    def save(self):
        save_name = tk.filedialog.asksaveasfilename(title=u'保存参数')
        if save_name == '':
            print("未成功保存")
            return 0
        save_name += '.npz'
        save_list = [self.filename.get(), self.Gauss_number, self.Lorentz_number, self.Voigt_number, self.Wave_number, self.Now_data]
        np.savez(save_name, save_list, self.fit_list)
        print("保存成功")
    
    #退出子窗口
    def confirm(self):
        global top_box
        for i in range(24):
            self.fit_list[i] = self.fit_list_var[i].get()
        top_box.destroy()
        
    #退出子窗口2
    def confirm2(self):
        global top_box2
        
        top_box2.destroy()

        
if __name__ == '__main__':
    input_para = verification_window()
    #print(input_para.filename.get())
    

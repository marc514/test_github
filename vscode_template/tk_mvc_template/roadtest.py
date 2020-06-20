#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import time
import threading
import sys
if sys.version < '3':	# py2
    PY3 = False
    import Tkinter as Tk
    import ttk
else:	# py3
    PY3 = True
    import tkinter as Tk  # Apollo的py3里没有Tk
    from tkinter import ttk
    import importlib
# try: import Tkinter as Tk; except ImportError: import tkinter as Tk

# import numpy as np
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# from cyber_py import cyber
# from modules.localization.proto.localization_pb2 import LocalizationEstimate
# from modules.canbus.proto.chassis_pb2 import Chassis
# from modules.planning.proto.planning_pb2 import ADCTrajectory

# View 界面
class View():
    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("Tk_MVC--roadtest_recorder")

        # Tab Control
        tabControl = ttk.Notebook(self.root)    # Create Tab Control
        tab1 = ttk.Frame(tabControl)            # Create a tab 
        tabControl.add(tab1, text='OnRoad')      # Add the tab
        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='Offline')      # Make second tab visible
        tabControl.pack(expand=1, fill="both")  # Pack to make visible

        # frame1 第1行按钮
        self.frame1 = Tk.Frame(tab1)
        self.cmbList = []
        self.cmbNoList = ('No.3', 'No.4')  # 可以不加self吗？
        self.cmbDriverList = ('WangChao', 'YuXin')
        self.cmbPurposeList = ('1:openLoop','2:closedLoop','3:RDtest',
                                '4:QAtest','5:dataClct','6:others')
        for i in range(3):
            self.cmbList.append(ttk.Combobox(self.frame1, 
                                            width = 20, height = 10))
            self.cmbList[i].grid(row=0, column=i)
            if i == 0:
                self.cmbList[i]['value'] = self.cmbNoList
                self.cmbList[i].current(0)
            elif i == 1:
                self.cmbList[i]['value'] = self.cmbDriverList
                self.cmbList[i].current(0)
            elif i == 2:
                self.cmbList[i]['value'] = self.cmbPurposeList
                self.cmbList[i].current(3)
        # self.frame1.grid(row=0, column=0, sticky='w')
        self.frame1.grid(row=0, column=0)

        # frame2 第2行按钮
        self.frame2 = Tk.Frame(tab1)
        self.buttonList = []
        self.buttonTextList = ["start", "stop", "take-over", "exception",
                               "unsafe", "uncomfortable", "export"]
        self.buttonColorList = ["LightSkyBlue", "SkyBlue", "DeepSkyBlue", "DodgerBlue", 
                                "RoyalBlue", "CornflowerBlue", "SteelBlue"]
        for i in range(7):
            self.buttonList.append(Tk.Button(self.frame2, 
                                            text=self.buttonTextList[i],
                                            bg=self.buttonColorList[i], 
                                            font=("Arial", 10),
                                            width=10, height=1))
            self.buttonList[i].grid(row=0, column=i)
        self.frame2.grid(row=1, column=0)


        # frame3 第3行时刻记录
        self.frame3 = Tk.Frame(tab1)
        self.textList = []
        for i in range(1):
            self.textList.append(Tk.Text(self.frame3, 
                                        font=("Arial", 10), 
                                        width=100, height=10))
            self.textList[i].grid(row=0, column=i)
        self.frame3.grid(row=2, column=0)

        # TODO: text框变化了！！！！！！！！！！！！！！！！
        # frame4 第4行文本框文本计数
        self.frame4 = Tk.Frame(tab1)
        self.varList = []
        self.entryList = []
        for i in range(7):
            self.varList.append(Tk.StringVar())
            self.varList[i].set(0)
            self.entryList.append(Tk.Entry(self.frame4, 
                                            textvariable=self.varList[i],
                                            font=("Arial", 10), 
                                            width=13))
            self.entryList[i].grid(row=0, column=i)
        # self.frame4.grid(row=3, column=0)
        # 整个frame4隐藏显示，代码可以简化
        # TODO: text框变化了！！！！！！！！！！！！！！！！


# Control 主体 交互操作
class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View()

        # for i in range(len(self.view.buttonList)):
        #     if i == (len(self.view.buttonList)-1):
        #         self.view.buttonList[i].config(
        #                                   command=lambda:self.clear_all())
        #     else:
        #         self.view.buttonList[i].config(
        #                                   command=lambda:self.print_time(i))
        # lambda表达式延时调用，点击时触发，此时i为6
        self.view.buttonList[0].config(command=lambda: self.print_time(0))
        self.view.buttonList[1].config(command=lambda: self.print_time(1))
        self.view.buttonList[2].config(command=lambda: self.print_time(2))
        self.view.buttonList[3].config(command=lambda: self.print_time(3))
        self.view.buttonList[4].config(command=lambda: self.print_time(4))
        self.view.buttonList[5].config(command=lambda: self.print_time(5))
        self.view.buttonList[6].config(command=lambda: self.clear_all())

    def run(self):
        self.view.root.mainloop()

    def print_time(self, buttonNo):
        self.view.varList[buttonNo].set(int(self.view.varList[buttonNo].get())+1)
        timeNow = time.strftime("%H-%M-%S", time.localtime())
        buttonMeanList = [' start recorder \n',' stop recorder \n', 
                        " take-over \n", " exception \n",
                        " unsafe \n", " uncomfortable \n"]
        self.view.textList[0].insert(Tk.END, timeNow + buttonMeanList[buttonNo])
        self.view.textList[0].see(Tk.END)
        if buttonNo == 0:
            roadtestConf = self.view.cmbList[0].get()[-1] + '\n' + \
                            self.view.cmbList[1].get() + '\n' + \
                            self.view.cmbList[2].get()[0] + '\n'
            roadtestConfYaml = open("roadtest_conf.yaml", "w+")
            roadtestConfYaml.write(roadtestConf)
            rt1 = recordThread(1, "thread1", 1)
            rt1.start()
        elif buttonNo == 1:
            # (ctrl+c) kill -2 cyber_recorder及父进程recorder.sh的pid
            os.system('kill -2 $(ps -ef | grep \'cyber_recorder\' | awk \'NR==1{print $2,$3}\')')            
    
    def clear_all(self):
        date = time.strftime("%Y-%m-%d", time.localtime())
        rtr = open(date+".txt", "a+")
        if PY3 == False:
            strDateTxt = '\n**********SUMMARY:**********\n' + \
                            self.view.textList[0].get(1.0, Tk.END).encode('utf-8') + \
                            '接管次数: ' + self.view.varList[2].get().encode('utf-8') + \
                            '\n异常次数: ' + self.view.varList[3].get().encode('utf-8') + \
                            '\n******************************\n'
        else:
            strDateTxt = '\n**********SUMMARY:**********\n' + \
                            self.view.textList[0].get(1.0, Tk.END) + \
                            '接管次数: ' + self.view.varList[2].get() + \
                            '\n异常次数: ' + self.view.varList[3].get() + \
                            '\n******************************\n'
        print (strDateTxt) # encode ascii 真坑
        rtr.write(strDateTxt)
        self.view.textList[0].delete(1.0, Tk.END)
        for v in self.view.varList:
            v.set(0)

    def get_value(self, numb):
        self.model.readChannel(numb)


# Model 数据模型
class Model():
    def __init__(self):
        # self.speed_mps = None
        pass

    def readChannel(self, numb):
        # TODO：预留yaml识别通道
        rt2 = readChannelThread(2, "thread2", 2)
        rt2.start()


class readChannelThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        # self.name = name
        # self.counter = counter

    def run(self):
        pass
        # cyber.init()
        # self.chassis_sub = cyber.Node('chassis_sub')
        # self.chassis_sub.create_reader('/apollo/canbus/chassis',
        #                                Chassis, self.callback_chassis)
        # self.chassis_sub.spin()


class recordThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        # self.name = name
        # self.counter = counter

    def run(self):
        os.system('/apollo/scripts/recorder.sh start -m < ./roadtest_conf.yaml')


if __name__ == '__main__':
    c = Controller()
    c.run()

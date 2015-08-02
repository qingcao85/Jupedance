#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#   A tool to analyse the results of impedance test of SOFC
#   by importing a Forthan programm 'ftikreg'.

import sys
import os
import shutil   #for move files
import glob
import ftikreg

######################### functions ############################
def getColumn(name, n1, n2):
    lines= open(name).readlines()
    open('temp.txt','w').writelines(lines[29:-1])
    with open("ftikreg.dat","w") as output:
        for x in open('temp.txt'):
            a= x.split()[n1-1]
            b= x.split()[n2-1]
            output.write(a)
            output.write("    ")
            output.write(b)
            output.write("\n")
        os.remove('temp.txt')
        return
def getColumnAll():
    s=glob.glob('*.txt')
    print(s)
    for tFile in s:
        lines= open(tFile).readlines()
        open('temp.txt','w').writelines(lines[29:-1])
        with open('ftikreg_'+tFile,"w") as output:
            for x in open('temp.txt'):
                a= x.split()[1]
                b= x.split()[2]
                output.write(a)
                output.write("    ")
                output.write(b)
                output.write("\n")
            os.remove('temp.txt')
    return
##########################################################

# programm start

print '帅哥你好,我是文件提取小助手,请选择模式==> 1.单文件模式  2.批处理模式(目前只提取2，3列):'
tp =int(raw_input())
if tp==1:
    n=[]
    print '请输入文件名:'
    name = raw_input()
    print '请输入想提取的第一列:'
    n.append(int(raw_input()))
    print '请输入想提取的第二列:'
    n.append(int(raw_input()))
    getColumn(name, n[0], n[1])
    print '提取完成! 现在使用 ftikreg 程序对频率和实部进行分析...'
    #run ftikreg programm
    ftikreg.main_routine()
    os.remove('ftikreg.adp')    #remove useless files
    os.remove('ftikreg.dat')
    shutil.move('ftikreg.sol', 'results/')
    print '分析完成! 结果保存在 ==> results/ftikreg.sol'

elif tp==2:
    getColumnAll()
    print '\033[91m'+'\033[1m'+'人生苦短，我用python!'+'\033[0m'
    print '提取完成！'
else:
    exit()

exit() # programm end

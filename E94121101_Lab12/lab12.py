import matplotlib.pyplot as plt
import numpy as np

def handlefile(f,tmpli1,li):
    for line in f.readlines(): # handle the list
        tmpli1.append(line.strip())
    for i in tmpli1[1:]:
        li.append(i.split(','))
    for i in range(len(li)):
        del li[i][0]
    for i in range(len(li)):
        for j in range(len(li[i])):
            li[i][j] = float(li[i][j])

with open('Temperature.txt') as f:
    tmpli1=[]
    li=[]
    fig = plt.figure(figsize=(12,6))
    fig.add_subplot(1,2,1)

    handlefile(f,tmpli1,li) # since li is an iterable object, it's similar to call by reference
    years = np.arange(2013,2022) # [2013,2022), pos nums
    months = np.arange(1,13) # [1,13)
    meanli=[] # store the average of the temp per month

    for i in range(0,12): # get mean temp per month in a stupid way
        meanli.append((li[0][i]+li[1][i]+li[2][i]+li[3][i]+li[4][i]+li[5][i]+li[6][i]+li[7][i]+li[8][i])/9)
    totalmean=round(sum(meanli)/12, 2)
    for i in range(0,12):
        meanli[i]=round(meanli[i], 2)
    totalmeanli=[] # in order to create the dashed line for all average temp
    for i in range(1,13):
        totalmeanli.append(totalmean)

#---------subplot 1---------

    plt.subplot(1,2,1)
    for i in range(len(li)):
        plt.plot(months, li[i], label=years[i])

    plt.title('Tainan Monthly Mean Temperature From 2013 to 2021')
    plt.xlabel('Month')
    plt.ylabel('Temperature in Degree C')
    plt.legend()

#---------subplot 2---------

    plt.subplot(1,2,2)
    for i in range(len(meanli)):
        plt.plot(months, meanli, c='red', marker='o')
        plt.text(months[i], meanli[i], s=meanli[i])
    plt.text(months[0], totalmeanli[0]+0.1, s=totalmeanli[0]) # that '+0.1' is a offset
    plt.plot(months,totalmeanli, ls='--', label='Mean of 9 Years')
    plt.xlabel('Month')
    plt.ylabel('Temperature in Degree C')
    plt.title('Tainan Monthly Mean Temperature Of 2013 to 2021')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

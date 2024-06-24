import matplotlib.pyplot as plt
import numpy as np

def handleFile(f,tmpli,li,ycoord,xcoord):
    for line in f.readlines():
        tmpli.append(line.strip())
    del tmpli[0]
    for i in tmpli:
        li.append(i.split(' '))
    
    for i in range(len(li)):
        for j in range(2):
            li[i][j]=float(li[i][j])
    for y,x in li:
        ycoord.append(y)
        xcoord.append(x)

def LSE(yfit,ycoord):
    tmp=0
    for i in range(len(yfit)):
        tmp += (ycoord[i]-yfit[i])**2
    return round(tmp/len(yfit), 5)

with open('oddExperiment.txt') as f:
    tmpli=[]
    li=[]
    ycoord=[]
    xcoord=[]
    handleFile(f,tmpli,li,ycoord,xcoord) # handle the list

    plt.scatter(xcoord,ycoord,label='Data')
    equation2 = np.poly1d(np.polyfit(xcoord,ycoord,2)) # for deg 2
    equation1 = np.poly1d(np.polyfit(xcoord,ycoord,1)) # for deg 1
    yfit2=[]
    yfit1=[]
    for i in xcoord:
        yfit2.append(equation2(i))
        yfit1.append(equation1(i))

    lb2 = "Fit of degree 2, LSE = "+ str(LSE(yfit2,ycoord))
    lb1 = "Fit of degree 1, LSE = "+ str(LSE(yfit1,ycoord))
    plt.plot(xcoord, yfit1, label=lb1)
    plt.plot(xcoord, yfit2, label=lb2)
    plt.legend()
    plt.title('oddExperiment Data')
    plt.show()
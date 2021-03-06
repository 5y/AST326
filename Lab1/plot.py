import numpy as np
import matplotlib.pylab as plt

x1=np.loadtxt('lab1_data1.txt')
x2=np.loadtxt('lab1_data2.txt')
x3=np.loadtxt('lab1_data3.txt')
x4=np.loadtxt('lab1_data4.txt')
x5=np.loadtxt('lab1_data5.txt')
x6=np.loadtxt('lab1_data6.txt')

#first data set plot
a=plt.plot(x1,'r',lw=3)
plt.legend(('1'),loc='upper center')
plt.figure()
#second data set plot
b=plt.plot(x2,'b',lw=3)
plt.legend(('2'),loc='upper center')
plt.figure()
#third data set plot
c=plt.plot(x3,'g',lw=3)
plt.legend(('3'),loc='upper center')
plt.figure()
#fourth data set plot
d=plt.plot(x4,'m',lw=3)
plt.legend(('4'),loc='upper center')
plt.figure()
#fifth data set plot
e=plt.plot(x5,'k',lw=3)
plt.figure()
#sixth data set plot
f=plt.plot(x6,'y',lw=3)


plt.title('Photon counts per sample vs. Time(ms)')
plt.xlabel('Time(ms)')
plt.ylabel('Counts per sample')
plt.figure()

hmin=0
hmax=12
hr=np.arange(hmin,hmax+1,1)

hist=np.zeros(hmax-hmin+1,dtype=np.int)
for i in hr:
    hist[i]=np.where(x1==i)[0].size
plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='red')
plt.figure()
for i in hr:
    hist[i]=np.where(x2==i)[0].size
plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='blue')
plt.figure()
for i in hr:
    hist[i]=np.where(x3==i)[0].size
plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='green')
plt.figure()
for i in hr:
    hist[i]=np.where(x4==i)[0].size
plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='magenta')
plt.figure()    
for i in hr:
    hist[i]=np.where(x5==i)[0].size
plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='black')
plt.figure()
for i in hr:
    hist[i]=np.where(x6==i)[0].size
plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='yellow')

#hist=np.array([np.where(y==i)[0].size for i in hr])
#plt.plot(hr,hist,drawstyle='step')

#plotting histograms
#n, bins, patches = plt.hist(y, facecolor='green', histtype='step',lw=2)
#plt.figure()
#n, bins, patches = plt.hist(z, facecolor='magenta', histtype='step',lw=2)
#plt.figure()
#n, bins, patches = plt.hist(w, facecolor='red', histtype='step',lw=2)
#plt.figure()
#n, bins, patches = plt.hist(t, facecolor='blue', histtype='step',lw=2)

#plt.title('Histogram Plots')
#plt.xlabel('Count')
#plt.ylabel('Frequency')

#plt.legend(('first data set: (0.001,10)','second data set: (0.001,100)','third data set: (0.01,100)','fourth data set: (0.1,100)'),bbox_to_anchor=(0.77, 0.5))
plt.show()

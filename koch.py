import matplotlib.pylab as plt
import numpy as np
import math

def koch(a,b,iterations):
    #Starting point of our original line
    a1=a[0] #0
    a2=a[1] #0
    
    #End points of our original line
    b1=b[0] #1
    b2=b[1]  #0
    #pod kakim naklonom stait nasha baza, chtobi potom dobovljat znachenia esli ona pod uglom
    theta = np.arctan((b2-a2)/(b1-a1))
    length = np.sqrt((a1-b1)**2+(a2-b2)**2)
    
    #first nearest point from a
    c1 = (2*a1+b1)/3.
    c2 = (2*a2+b2)/3.
    c = [c1,c2]
    #second last point from a
    d1 = (a1+2*b1)/3.
    d2 = (a2+2*b2)/3.
    d = [d1,d2]

    
    if c1 >= a1:
        m1 = c1 + (length/3.)*math.cos(theta+math.pi/3.)
        m2 = c2 + (length/3.)*math.sin(theta+math.pi/3.)
    else:
        m1 = c1 + (length/3.)*math.cos(theta-2*math.pi/3.)
        m2 = c2 + (length/3.)*math.sin(theta-2*math.pi/3.)
    m = [m1,m2]
    
    c = np.array(c)
    d = np.array(d)
    m = np.array(m)
    
    points = []
    
    if iterations == 0:
        points.extend([a,b])
    elif iterations == 1:
        points.extend([a, c, m, d, b])
    else:
        points.extend(koch(a,c,iterations-1)) #Rekursija
        points.extend(koch(c,m,iterations-1))
        points.extend(koch(m,d,iterations-1))
        points.extend(koch(d,b,iterations-1))  
                        
    return points


n=int(input("Glubina rekursii:"))
plt.figure(figsize=(10,7))

points1 = koch(a=np.array([0, 0]),b=np.array([0.5,1]),iterations=n)
ptsx1=[]
ptsy1=[]
for i in range(len(points1)):
    ptsx1.append(points1[i][0])
    ptsy1.append(points1[i][1])
plt.plot(ptsx1, ptsy1, '-')
plt.axis('equal')
plt.axis('off')

points2 = koch(a=np.array([0.5, 1]),b=np.array([1,0]),iterations=n)
ptsx2=[]
ptsy2=[]
for i in range(len(points2)):
    ptsx2.append(points2[i][0])
    ptsy2.append(points2[i][1])
plt.plot(ptsx2, ptsy2, '-')
plt.axis('equal')
plt.axis('off')

points3 = koch(a=np.array([1, 0]),b=np.array([0,0]),iterations=n)
ptsx3=[]
ptsy3=[]
for i in range(len(points3)):
    ptsx3.append(points3[i][0])
    ptsy3.append(points3[i][1])
plt.plot(ptsx3, ptsy3, '-')
plt.axis('equal')
plt.axis('off')

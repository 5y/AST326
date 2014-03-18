import numpy as np
import matplotlib.pylab as plt

a=2.766 #semimajor axis(Au)
tau=2454868 #epoch of perihelion(Julian Date)
#t=2456667 #current epoch(Julian Date)
#v= #True anomaly(rad)
w_deg=73.12 #Arguement of perihelion(deg)
w=(w_deg*np.pi)/180 #w in rad
e=0.079 #eccentricity

omega_deg=80.72 #Longitude of ascending node(deg)
omega=(omega_deg*np.pi)/180
i_deg=10.61 #inclination(deg)
i=(i_deg*np.pi)/180 #i in rad

M_sun=2*(10**30) #mass of the Sun (kg)
G=6.67*(10**(-11)) #gravitational constant (SI units)

#k=np.sqrt(G*M_sun)
k=0.017202098950
n=k*(a**(-3./2))
p=(2*(np.pi))/n
t=np.arange(tau,(tau+p))

mu=n*(t-tau)

E=np.zeros(len(mu)) #Eccentric anomaly(rad)
E[0]=mu[0]
M=np.zeros(len(mu))
M[0]=E[0]
r=np.zeros(len(mu))


################# calculating M and E numerically ###############
for q in range(1,len(t)):
    M[q-1]=E[q-1]-e*(np.sin(E[q-1]))
    E[q]=E[q-1]+((mu[q-1]-M[q-1])/(1-e*np.cos(E[q-1])))
    

f=(np.sqrt(1+e/1-e))*(np.tan(E/2))
v=2*np.arctan(f)
theta=v+w #Polar angle from the x-axis(rad)
r=a*(1-(e*np.cos(E)))

##################### r vector values ########################
r_0=3 #Au

#r_x=r*((np.cos(omega))*(np.cos(theta))-((np.sin(omega))*(np.cos(i))*(np.sin(theta))))
#r_y=r*((np.sin(omega))*(np.cos(theta))+((np.cos(omega))*(np.cos(i))*(np.sin(theta))))
#r_z=r*(np.sin(i))*(np.sin(theta))

r_x=r*(np.cos(theta))
r_y=r*(np.sin(theta))
r_z=0


circle_x=a*(np.cos(theta))
circle_y=a*(np.sin(theta))


############### Section 4, step 3 (lambda and beta)  #################
lambda1=(121.7592648*np.pi)/180 #radians
lambda2=(122.1865441*np.pi)/180 #radians
lambda3=(122.6133849*np.pi)/180 #radians
beta1=(4.0625653*np.pi)/180 #radians
beta2=(4.0992581*np.pi)/180 #radians
beta3=(4.1361592*np.pi)/180 #radians



###### right ascension and declination values #############

alpha=[ 0.77589496, 0.77991461,0.78825718,0.79249126]
delta=[ 0.33553406,0.33640024, 0.33765579, 0.33851884]




######## equation 61, equatorial coordinates #########

x1_eqt=(np.cos(alpha[0]))*(np.cos(delta[0]))
y1_eqt=(np.sin(alpha[0]))*(np.cos(delta[0]))
z1_eqt=(np.sin(delta[0]))
x2_eqt=(np.cos(alpha[1]))*(np.cos(delta[1]))
y2_eqt=(np.sin(alpha[1]))*(np.cos(delta[1]))
z2_eqt=(np.sin(delta[1]))
x3_eqt=(np.cos(alpha[2]))*(np.cos(delta[2]))
y3_eqt=(np.sin(alpha[2]))*(np.cos(delta[2]))
z3_eqt=(np.sin(delta[2]))

epsilon=(23.43929111*(np.pi))/180  # epsilon value in radians



x1=x1_eqt
x2=x2_eqt
x3=x3_eqt
y1=((np.cos(epsilon))*y1_eqt)+((np.sin(epsilon))*z1_eqt)
y2=((np.cos(epsilon))*y2_eqt)+((np.sin(epsilon))*z2_eqt)
y3=((np.cos(epsilon))*y3_eqt)+((np.sin(epsilon))*z3_eqt)
z1=((-np.sin(epsilon))*y1_eqt)+((np.cos(epsilon))*z1_eqt)
z2=((-np.sin(epsilon))*y2_eqt)+((np.cos(epsilon))*z2_eqt)
z3=((-np.sin(epsilon))*y3_eqt)+((np.cos(epsilon))*z3_eqt)

# s vectors (equation 60)
s1=[x1,y1,z1]
s2=[x2,y2,z2]
s3=[x3,y3,z3]


################## s derivatives, equation 50 #############
t1=2455946.68646
t2=2455947.69476
t3=2455949.73866
tau1=t2-t1
tau3=t3-t2

#### s2 dot components
s2_dot_x=((tau3*(s2[0]-s1[0]))/(tau1*(tau1+tau3)))+((tau1*(s3[0]-s2[0]))/(tau3*(tau1+tau3)))
s2_dot_y=((tau3*(s2[1]-s1[1]))/(tau1*(tau1+tau3)))+((tau1*(s3[1]-s2[1]))/(tau3*(tau1+tau3)))
s2_dot_z=((tau3*(s2[2]-s1[2]))/(tau1*(tau1+tau3)))+((tau1*(s3[2]-s2[2]))/(tau3*(tau1+tau3)))
s2_dot=[s2_dot_x,s2_dot_y,s2_dot_z]  # s2 array

#### s2 dotdot components


s2_dotdot_x=((2*(s3[0]-s2[0]))/(tau3*(tau1+tau3)))-((2*(s2[0]-s1[0]))/(tau1*(tau1+tau3)))
s2_dotdot_y=((2*(s3[1]-s2[1]))/(tau3*(tau1+tau3)))-((2*(s2[1]-s1[1]))/(tau1*(tau1+tau3)))
s2_dotdot_z=((2*(s3[2]-s2[2]))/(tau3*(tau1+tau3)))-((2*(s2[2]-s1[2]))/(tau1*(tau1+tau3)))
s2_dotdot=[s2_dotdot_x,s2_dotdot_y,s2_dotdot_z] # s2 dotdot array

#s2_dotdot=[3.6914851e-05,-4.3035117e-05,3.5967350e-06]



##### R components of the second date(s2)
X2=-0.4974148410812385
Y2= 0.8490994851434150
Z2=-2.462584044959891*(10**(-05))

R2=[X2,Y2,Z2]
R_length=np.sqrt((X2**2)+(Y2**2)+(Z2**2))

R1 = [-0.4820742567460204,  0.8578010618775774, -2.425231096584922*(10**(-05))]
R3 = [-0.5280130493076013,  0.8306420761670466, -2.515673232526080*(10**(-05))]
R4 = [-0.5419538025371889,  0.8217251214639645, -2.524538626668697*(10**(-05))]



R2_dot_x=((tau3*(R2[0]-R1[0]))/(tau1*(tau1+tau3)))+((tau1*(R3[0]-R2[0]))/(tau3*(tau1+tau3)))
R2_dot_y=((tau3*(R2[1]-R1[1]))/(tau1*(tau1+tau3)))+((tau1*(R3[1]-R2[1]))/(tau3*(tau1+tau3)))
R2_dot_z=((tau3*(R2[2]-R1[2]))/(tau1*(tau1+tau3)))+((tau1*(R3[2]-R2[2]))/(tau3*(tau1+tau3)))
R2_dot=[R2_dot_x,R2_dot_y,R2_dot_z]  # s2 array


########### R*s2


R_s=[R2[1]*s2[2]-R2[2]*s2[1],R2[2]*s2[0]-R2[0]*s2[2],R2[0]*s2[1]-R2[1]*s2[0]]
s_dotdot_s=[s2_dotdot[1]*s2[2]-s2_dotdot[2]*s2[1],s2_dotdot[2]*s2[0]-s2_dotdot[0]*s2[2],s2_dotdot[0]*s2[1]-s2_dotdot[1]*s2[0]]

sdot_R_s=(R_s[0]*s2_dot[0])+(R_s[1]*s2_dot[1])+(R_s[2]*s2_dot[2])
sdot_s_dotdot_s=(s2_dot[0]*s_dotdot_s[0])+(s2_dot[1]*s_dotdot_s[1])+(s2_dot[2]*s_dotdot_s[2])

################ computing rho and r (step 6) ####################

denom=(sdot_R_s)/(sdot_s_dotdot_s)
rho=((k**2)*((1./(R_length**3))-(1./(r_0**3))))*denom
R_dot_s=(R2[0]*s2[0])+(R2[1]*s2[1])+(R2[2]*s2[2])

### equation 48
r1=np.sqrt((rho**2)+(R_length**2)+(2*rho*R_dot_s)) #Au

################## plots ######################
plt.plot(t,mu,'-b',t,E,'r')
plt.title('Mean Anomaly, M and Eccentric Anomaly E for the asteroid Ceres')
plt.xlabel('time[Julian Date]')
plt.ylabel('Anomaly[radians]')
plt.legend(('Mean Anomaly','Eccentric Anomaly'),loc='best')
plt.figure(figsize=(8,3))

plt.plot(t,r)
plt.title('Orbital Separation r as a function of time')
plt.title('position of the asteroid')
plt.xlabel('time[Julian Day]')
plt.ylabel('r[Au]')
plt.figure(figsize=(8,3))

plt.plot(t,v)
plt.title('True Anomaly as a function of time')
plt.xlabel('Time[Julian Date]')
plt.ylabel('v[radians]')
plt.figure()

plt.plot(r_x,r_y)
plt.title('The position of Ceres in the plane of the orbit')
plt.xlabel('x [Au]')
plt.ylabel('y [Au]')
plt.plot(circle_x,circle_y,'--m')
plt.plot(r_x[0],r_y[0],'o')
plt.legend(('position of Ceres','circle with radius a'),loc='best')
plt.plot(0,0,'+g')

plt.show()

# homework Question 1
import math
import numpy as np
import matplotlib.pyplot as plt
fig,axes=plt.subplots(nrows=1,ncols=3)
plt.subplots_adjust(hspace=0.2,wspace=0.2)
theta=np.linspace(0,2*np.pi,1000)
#Make a plot of the so-called deltoid curve, which is defined parametrically by the equations, x = 2 cos θ + cos 2θ, y = 2 sin θ − sin 2θ, where 0 ≤ θ < 2π. Take a set of values of θ between zero and 2π and calculate x and y for each from the equations above, then plot y as a function of x
#x = 2 cos θ + cos 2θ, y = 2 sin θ − sin 2θ
x=2*np.cos(theta)+np.cos(2*theta)
y=2*np.sin(theta)-np.sin(2*theta)
axes[0].plot(x,y)
axes[0].set_title('Deltoid Curve')
# plt.show()


# Homework question 1b
# r = f(θ) ,x = r cos θ, y = r sin θ,  r=θ2 for 0 ≤ θ ≤ 10π
# problem 1(b) Galilean spiral
theta_1=np.linspace(0,10*np.pi,10000)
r=(theta_1)**2
x_1=r*np.cos(theta_1)
y_1=r*np.sin(theta_1)
# plt.subplot(2,2,1)
axes[1].plot(x_1,y_1)
axes[1].set_title('Galilean Spiral')


# problem 1(c)Fey's Function 
theta_2=np.linspace(0,24*np.pi,10000)
r_1=np.exp(np.cos(theta_2)) - 2*np.cos(4*theta_2) + (np.sin(theta_2/12))**5
x_2=r_1*np.cos(theta_2)
y_2=r_1*np.sin(theta_2)
axes[2].plot(x_2,y_2)
axes[2].set_title('Fey funciton')
plt.show()

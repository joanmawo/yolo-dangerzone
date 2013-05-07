import sys
import os
import pylab
import numpy as np
import scipy

#Programa que ajusta parametros de un modelo a observaciones con el metodo de cadenas de markov. El programa recibe las observaciones del archivo "traces.dat"

obs_data = np.loadtxt("traces.dat")
x1_obs = obs_data[:,0]
y1_obs = obs_data[:,1]
z1_obs = obs_data[:,2]
x2_obs = obs_data[:,3]
y2_obs = obs_data[:,4]
z2_obs = obs_data[:,5]

n_iterations = 40000
limite_x = 20
tolerancia_x = 10
limite_y = -22
tolerancia_y = 10
limite_z = -3950
tolerancia_z = 100


x1_walk = np.empty((0)) #this is an empty list to keep all the steps
x1_0 = (np.random.random()*tolerancia_x + limite_x) #this is the initialization
x1_walk = np.append(x1_walk,x1_0)

x2_walk = np.empty((0)) #this is an empty list to keep all the steps
x2_0 = (np.random.random()*tolerancia_y + limite_y) #this is the initialization
x2_walk = np.append(x2_walk,x2_0)

x3_walk = np.empty((0)) #this is an empty list to keep all the steps
x3_0 = (np.random.random()*tolerancia_z + limite_z) #this is the initialization
x3_walk = np.append(x3_walk,x3_0)



def likelihood(x2_obs, y2_obs, x, y):
    chi_squared = sum(((x2_obs - x)**2 + (y2_obs - y)**2))
    return -chi_squared

def my_model_x(x1_obs, z2_obs, xo, zo):
	x = (z2_obs - zo)*(x1_obs - xo)/(-zo)
	return x

def my_model_y(y1_obs, z2_obs, yo, zo):
	y = (z2_obs - zo)*(y1_obs - yo)/(-zo)
	return y



for i in range(n_iterations):
    	#0.1 is the sigma in the normal distribution
	x1_prime = np.random.normal(x1_walk[i], 0.1) 
	x2_prime = np.random.normal(x2_walk[i], 0.1)
	x3_prime = np.random.normal(x3_walk[i], 0.1)

	x_init  = my_model_x(x1_obs, z2_obs, x1_walk[i], x3_walk[i])
    	x_prime = my_model_x(x1_obs, z2_obs, x1_prime, x3_prime)
	y_init  = my_model_x(y1_obs, z2_obs, x2_walk[i], x3_walk[i])
    	y_prime = my_model_x(y1_obs, z2_obs, x2_prime, x3_prime)

    	alpha = likelihood(x2_obs, y2_obs, x_prime, y_prime) -likelihood(x2_obs, y2_obs, x_init, y_init)
	
    	if(alpha > 0.0):
        	x1_walk = np.append(x1_walk, x1_prime)
		x2_walk = np.append(x2_walk, x2_prime)
		x3_walk = np.append(x3_walk, x3_prime)
   	else:
       		beta = np.random.random()
        	if(beta < np.exp(alpha)):
            		x1_walk = np.append(x1_walk,x1_prime)
			x2_walk = np.append(x2_walk,x2_prime)
			x3_walk = np.append(x3_walk,x3_prime)
      		else:
            		x1_walk = np.append(x1_walk,x1_walk[i])
			x2_walk = np.append(x2_walk,x2_walk[i])
			x3_walk = np.append(x3_walk,x3_walk[i])


average_x1 = np.average(x1_walk)
average_x2 = np.average(x2_walk)
average_x3 = np.average(x3_walk)

fx = open("x.txt", "w")
for item in x1_walk:
	fx.write("%f \n" % item)
fx.close()

fy = open("y.txt", "w")
for item in x2_walk:
	fy.write("%f \n" % item)
fy.close()

fz = open("z.txt", "w")
for item in x3_walk:
	fz.write("%f \n" % item)
fz.close()




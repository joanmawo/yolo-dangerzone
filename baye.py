import sys
import os
import pylab
import numpy as np
import scipy

#Programa que ajusta parametros de un modelo a observaciones con el metodo de cadenas de markov. El programa recibe las observaciones del archivo "movimiento.dat"

obs_data = np.loadtxt("traces.dat")
x1 = obs_data[:,0]
y1 = obs_data[:,1]
z1 = obs_data[:,2]
x2 = obs_data[:,3]
y2 = obs_data[:,4]
z2 = obs_data[:,5]

n_iterations = 200000 

x1_walk = np.empty((0)) #this is an empty list to keep all the steps
x1_0 = (np.random.random()) #this is the initialization
x1_walk = np.append(x1_walk,x1_0)

x2_walk = np.empty((0)) #this is an empty list to keep all the steps
x2_0 = (np.random.random()) #this is the initialization
x2_walk = np.append(x2_walk,x2_0)

x3_walk = np.empty((0)) #this is an empty list to keep all the steps
x3_0 = (np.random.random()) #this is the initialization
x3_walk = np.append(x3_walk,x3_0)



def likelihood(y_obs, y_model):
    chi_squared = sum((y_obs - y_model)**2)
    return np.exp(-chi_squared)

def my_model(t_obs, a1, a2, a3):
	return a1 + a2*t_obs + a3*t_obs*t_obs

for i in range(n_iterations):
    	#0.1 is the sigma in the normal distribution
	x1_prime = np.random.normal(x1_walk[i], 0.1) 
	x2_prime = np.random.normal(x2_walk[i], 0.1)
	x3_prime = np.random.normal(x3_walk[i], 0.1)

	y_init = my_model(t_obs, x1_walk[i], x2_walk[i], x3_walk[i])
    	y_prime = my_model(t_obs, x1_prime, x2_prime, x3_prime)

    	alpha = likelihood(y_obs, y_prime)/likelihood(y_obs, y_init)
	
    	if(alpha >= 1.0):
        	x1_walk = np.append(x1_walk, x1_prime)
		x2_walk = np.append(x2_walk, x2_prime)
		x3_walk = np.append(x3_walk, x3_prime)
   	else:
       		beta = np.random.random()
        	if(beta<=alpha):
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

best_y = my_model(t_obs, average_x1, average_x2, average_x3)

pylab.scatter(t_obs, y_obs)
pylab.plot(t_obs, best_y, 'b')
pylab.xlabel('tiempo')
pylab.ylabel('posicion vertical')
pylab.savefig("ajuste.png")
pylab.show()


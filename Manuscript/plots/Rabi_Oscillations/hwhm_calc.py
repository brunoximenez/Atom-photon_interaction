import numpy as np
'''
Solving t_pi x rabi width from the notes
'''
c0 = np.sqrt(2)/np.pi - 1
c1 = 0
c2 = 1/6
c3 = 0
c4 = -1/120
c5 = 0
c6 = 1/(120*42)

coeff = [c6, c5, c4, c3, c2, c1, c0]
solutions = np.roots(coeff)

for s in solutions:
    if np.imag(s) == 0:
        x = np.real(s) #  There are two solution whose abs value is equal

t_sigma = np.sqrt( np.square(2*x/np.pi) - 1 )
print(t_sigma)

'''
Now for the fourier spectrum of the laser
'''

c0 = -1/2
coeff = [c6, c5, c4, c3, c2, c1, c0]
solutions = np.roots(coeff)

for s in solutions:
    if np.imag(s) == 0:
        x = np.real(s) #  There are two solution whose abs value is equal

t_pi = 0.2
t_sigma = 4*x/(t_pi*2*np.pi)
print(t_sigma)
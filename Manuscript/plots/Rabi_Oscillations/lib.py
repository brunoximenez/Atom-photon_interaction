from scipy import constants
import numpy as np

pi = constants.pi

def omega_(t_pi, detuning):
    omega = t_pi * (2 * pi * detuning) / pi
    omega = np.square(omega)
    omega = 1 + omega
    omega = np.sqrt(omega)
    return omega


def rabi_oscillations(t, t_pi, detuning):
    theta = omega_(t_pi, detuning) * pi * t / (t_pi * 2)
    theta = np.sin(theta)
    theta = np.square(theta)
    osc = theta / np.square(omega_(t_pi, detuning))
    return osc

import qutip as qu
import numpy as np
import matplotlib.pyplot as plt

b = qu.Bloch()


def bloch_rabi(t, detuning, t_pi):
    omega_r = np.pi / (2 * t_pi)
    omega_ = np.sqrt(np.square(detuning) + 4 * np.square(omega_r))

    z = np.square(detuning) - 4 * np.square(omega_r)
    z = z * np.sin(omega_ * t / 2) / np.square(omega_)
    z = z + np.cos(omega_ * t / 2)

    y = (4 * omega_r / omega_) * \
        np.sin(omega_ * t / 2) * np.cos(omega_ * t / 2)

    x = 4 * omega_r * detuning * \
        np.square(np.sin(omega_ * t / 2)) / np.square(omega_)
    return [x,y,z]

t_pi = 0.01
t = 0
vec = bloch_rabi(t, 100, t_pi)

b.add_vectors(vec)
t = t_pi
vec = bloch_rabi(t, 0, t_pi)
b.add_vectors(vec)
# b.sphere_alpha(0.1)
# b.font_color('red')
# b.zlabel('$\\left|0\\right>$', '$\\left|1\\right>$')

b.save('test.png')
b.show()


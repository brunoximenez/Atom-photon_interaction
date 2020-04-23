import sys
import matplotlib.pyplot as plt
import numpy as np
import lib as lb

pi = np.pi

t_pi = 0.01
width = 0.8 / t_pi
detuning_min = -5*width
detuning_max = 5*width
detunings = np.linspace(detuning_min, detuning_max, 1000)


t = np.array([t_pi, t_pi/2, 2*t_pi])
label= np.array(['t = $t_{\pi}$', 't = $t_{\pi}$ / 2', 't = $2t_{\pi}$'])
for t, label in zip(t, label):
    profile = lb.rabi_oscillations(t, t_pi, detunings)
    plt.subplot(122)
    plt.plot(detunings, profile, label=label)

plt.legend(shadow=True)
plt.xlim((detuning_min, detuning_max))
plt.ylim((0, 1))
fontsize = 14
plt.xlabel('$\Delta$ (Hz)', fontsize=fontsize)
plt.ylabel('$P_{e}$($\Delta$, $t_{\pi}$ = 10 ms)', fontsize=fontsize)

t_max = 5*t_pi
t = np.linspace(0, t_max, 500)
detuning_oscillations = np.array([0, 50, 100])
for d in detuning_oscillations:
    label = '$\Delta$ =' + str(d) + ' Hz'
    osc = lb.rabi_oscillations(t, t_pi, d)
    plt.subplot(121)
    plt.plot(t, osc, label=label)

plt.xlim((0, t_max))
plt.ylim((0, 1))
plt.ylabel('$P_{e}$(t, $t_{\pi}$ = 10 ms)', fontsize=fontsize)
plt.xlabel('t (s)', fontsize=fontsize)
plt.legend(shadow=True, fontsize=fontsize)
plt.show()
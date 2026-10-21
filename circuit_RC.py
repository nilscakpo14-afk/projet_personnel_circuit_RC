# Analyse d'un circuit RC
import numpy as np
import matplotlib.pyplot as plt

# Diagramme de Bode

# Filtre passe bas
f = np.array([0.1, 0.2, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 2, 5]) # fréquence du générateur en Hz
Ve = np.array([5.18, 5.15, 5.17, 5.17, 5.17, 5.15, 5.15, 5.16, 5.16, 5.18, 5.18, 5.15, 5.15, 5.18, 5.15, 5.15]) # tension du générateur en V
Vs = np.array([5.09, 4.94, 4.25, 4.01, 3.78, 3.64, 3.55, 3.32, 3.12, 2.94, 2.79, 2.62, 2.50, 2.38, 1.88, 0.88]) # tension de sortie du condensateur en V
phi = -np.array([7.22, 13.95, 31.83, 37.46, 42.46, 44.10, 45.53, 48.19, 52.24, 54.58, 56.97, 57.07, 61.17, 60.74, 66.71, 75.93]) # déphasage tension du condensateur par rapport a la tension du générateur en degré

G = Vs/Ve # gain
G_dB = 20*np.log10(G) # gain en dB


# théories

taux = 211.35e-3 # temps caracteristique du circuit RC en s

fc = 1/(2*np.pi*taux) # frequence de coupure du cicuit RC en Hz

f_th = np.linspace(0, 10, 100) # fréquence du générateur en Hz
G_dB_th = 20*np.log10(1/np.sqrt(1+(f_th/fc)**2)) # gain theorique en dB
phi_th = -np.arctan(f_th/fc)*180/np.pi # déphasage theorique en degre

# tracer du diagramme

fig, ax = plt.subplots(2, 1)

ax[0].scatter(f, G_dB, color = 'b')
ax[0].plot(f, G_dB, color = 'b', label = 'gain expérimental')
ax[1].scatter(f, phi, color = 'b')
ax[1].plot(f, phi, color = 'b', label = 'dephasage experiemental')

ax[0].plot(f_th, G_dB_th, color = 'r', label = 'gain theorique')
ax[1].plot(f_th , phi_th, color = 'r', label = 'dephasage theorique')


ax[0].set_xlabel('fréquence en Hz')
ax[0].set_ylabel('gain en dB')
ax[1].set_xlabel('fréquence en Hz')
ax[1].set_ylabel('dephasage en degre')
ax[0].set_xscale('log')
ax[1].set_xscale('log')
fig.suptitle('diagramme de bode circuit RC (filtre passe bas)')

ax[0].legend()
ax[1].legend()

plt.tight_layout()
plt.show()

# Filtre passe haut

Ve = np.array([5.19, 5.16, 5.18, 5.16, 5.14, 5.15, 5.16, 5.18, 5.15, 5.17, 5.15, 5.18, 5.15, 5.13, 5.13, 5.13]) # tension du gérérateur en V
Vr = np.array([0.84, 1.47, 2.96, 3.30, 3.57, 3.71, 3.80, 3.98, 4.17, 4.28, 4.39, 4.49, 4.55, 4.61, 4.83, 5.09]) # tension de la résistance en V
phi_r = np.array([92.22, 78.17, 55.89, 50.88, 47.41, 46.65, 43.03, 40.18, 36.60, 36.31, 32.61, 32.05, 28.27, 26.76, 21.30, 9.00]) # dephasage résistance generateur

Gr = Vr/Ve # gain résistance generateur
Gr_dB = 20*np.log10(Gr) # gain resistance générateur en dB

# théories

taux = 211.35e-3 # temps caracteristique du circuit RC en s

fc = 1/(2*np.pi*taux) # frequence de coupure du cicuit RC en Hz

f_th = np.linspace(0, 10, 100) # fréquence du générateur en Hz
Gr_dB_th = 20*np.log10((f_th/fc)/np.sqrt(1+(f_th/fc)**2)) # gain theorique ur/ue en dB
phi_r_th = np.arctan(fc/f_th)*180/np.pi # déphasage ur/ue theorique en degre

# tracer du diagramme

fig, ax = plt.subplots(2, 1)

ax[0].scatter(f, Gr_dB, color = 'b')
ax[0].plot(f, Gr_dB, color = 'b', label = 'gain expérimental')
ax[1].scatter(f, phi_r, color = 'b')
ax[1].plot(f, phi_r, color = 'b', label = 'dephasage experiemental')

ax[0].plot(f_th, Gr_dB_th, color = 'r', label = 'gain theorique')
ax[1].plot(f_th , phi_r_th, color = 'r', label = 'dephasage theorique')


ax[0].set_xlabel('fréquence en Hz')
ax[0].set_ylabel('gain en dB')
ax[1].set_xlabel('fréquence en Hz')
ax[1].set_ylabel('dephasage en degre')
ax[0].set_xscale('log')
ax[1].set_xscale('log')
fig.suptitle('diagramme de bode circuit RC (filtre passe haut)')

ax[0].legend()
ax[1].legend()

plt.tight_layout()
plt.show()

print("Interprétation: Un gain en dB qui tend vers 0 indique que le composant electrique laisse passer la tension du générateur a une frequence donnée. Au contraire un gain qui tend vers les valeur négative indique que le composant électrique s'oppose au passe de la tension du générateur")
print("c'est pourquoi les diagramme montrent que la sortie de la résistance est un filtre passe haut et celle du condensateur un filtre passe bas")
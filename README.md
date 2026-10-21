# Filtre passe bas/passe haut et diagramme de Bode

## Objectif

Il s'agit de réaliser un filtre passe bas/passe haut et de tracer le diagramme de Bode correspondant.

## I. Filtre passe bas

Nous disposons d'un circuit RC alimenté par un générateur de frequence f avec une tension sinusoidale variant entre 0 et 5V. 

Le déphasage $\phi$ de la tension du condensateur par rapport a la tension du circuit (generateur) sécrit:
$$
\phi = -\arctan(\frac{f}{f_c})
$$
avec 
$$
f_c = \frac{2\pi}{RC}
$$ la frequence de coupure du circuit

Le gain G quand a lui s'écrit:
$$
G_{C,th} = \frac{1}{\sqrt{1+\frac{f}{f_c}^2}}
$$
$$
G_{C,exp} = \frac{V_C}{V_e}
$$
resp. le gain théorique et le gain expérimentale avec $V_c$ et $V_e$ les tensions crete a crete du condensateur et du générateur


## II. Filtre passe haut

On fait des mesure de manière analogue au niveau de la résistance R.

$$
\phi_R = \arctan(\frac{f_c}{f})
$$
$$
G_{R,th} = \frac{\frac{f}{f_c}}{\sqrt{1+\frac{f}{f_c}^2}}
$$
$$
G_{R,exp} = \frac{V_R}{V_e}
$$

avec
$$ V_R = V_e - V_C$$

Remarque: les déphasages expérimentaux sont lus sur l'oscilloscope. 

De plus, le gain en décibel $G_{dB}$ s'exprime de la manière suivante:
$$
G_{\mathrm{dB}} = 10\log_{10}(G)
$$

## Traitement des données

python

## Fichiers

- 'circuit RC' traitement des données 

## Auteur

Nils CAKPO
L3 Physique
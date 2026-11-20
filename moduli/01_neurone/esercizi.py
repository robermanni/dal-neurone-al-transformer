"""Modulo 1 – Esercizi.

Completa le funzioni sostituendo `raise NotImplementedError` con il tuo codice.
Poi verifica il tuo lavoro dalla cartella principale del progetto:

    python -m pytest moduli/01_neurone --studente

Convenzioni: X è una matrice (n_punti, n_caratteristiche), w un vettore
di pesi, b un numero (bias), y un vettore di etichette con valori -1 o +1.
"""
import numpy as np


def distanza_firmata(X, w, b):
    """Distanza con segno di ogni punto di X dal confine di decisione.

    È positiva dal lato verso cui punta w, negativa dall'altro, zero sul confine.
    Suggerimento: il punteggio w·x + b va diviso per la norma di w.
    Se w è il vettore nullo, solleva ValueError.

    Esempio:
        >>> distanza_firmata([[3, 4]], w=[3, 4], b=0)
        array([5.])
    """
    raise NotImplementedError("Da completare")


def margine(X, y, w, b):
    """Il margine del classificatore sul dataset (X, y).

    È la più piccola tra le distanze firmate moltiplicate per l'etichetta:
    min_i  y_i * distanza_i.
    È positivo solo se TUTTI i punti sono classificati correttamente,
    e il suo valore dice quanto il punto "più a rischio" è lontano dal confine.
    Restituisci un float.
    """
    raise NotImplementedError("Da completare")


def addestra_percettrone(X, y, max_epoche=100):
    """Addestra un percettrone con la regola di Rosenblatt.

    Parti da w nullo e b = 0. A ogni epoca scorri i punti nell'ordine dato;
    se un punto è classificato male (y_i * (w·x_i + b) <= 0) aggiorna:
        w <- w + y_i * x_i
        b <- b + y_i
    Conta gli errori di ogni epoca. Fermati appena un'epoca ha zero errori,
    oppure dopo max_epoche.

    Restituisce: (w, b, errori) dove errori è la lista degli errori per epoca.
    """
    raise NotImplementedError("Da completare")


def confine_retta(w, b, x1):
    """Per un classificatore in 2D, la coordinata x2 del confine per ogni x1.

    Il confine è dove w[0]*x1 + w[1]*x2 + b = 0: ricava x2.
    Se w[1] è zero il confine è una retta verticale e non si può scrivere
    come funzione di x1: in quel caso solleva ValueError.
    """
    raise NotImplementedError("Da completare")

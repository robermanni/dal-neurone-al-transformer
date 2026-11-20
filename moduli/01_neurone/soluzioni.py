"""Modulo 1 – Soluzioni di riferimento.

Prova prima a risolvere gli esercizi in esercizi.py: leggere la soluzione
insegna molto meno che scriverla.
"""
import numpy as np


def distanza_firmata(X, w, b):
    X = np.atleast_2d(np.asarray(X, dtype=float))
    w = np.asarray(w, dtype=float)
    norma = np.linalg.norm(w)
    if norma == 0:
        raise ValueError("Il vettore dei pesi w non può essere nullo.")
    return (X @ w + b) / norma


def margine(X, y, w, b):
    y = np.asarray(y, dtype=float)
    return float(np.min(y * distanza_firmata(X, w, b)))


def addestra_percettrone(X, y, max_epoche=100):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    w = np.zeros(X.shape[1])
    b = 0.0
    errori = []
    for _ in range(max_epoche):
        n_errori = 0
        for xi, yi in zip(X, y):
            if yi * (xi @ w + b) <= 0:
                w = w + yi * xi
                b = b + yi
                n_errori += 1
        errori.append(n_errori)
        if n_errori == 0:
            break
    return w, b, errori


def confine_retta(w, b, x1):
    if w[1] == 0:
        raise ValueError("Con w[1] = 0 il confine è verticale: x2 non è funzione di x1.")
    return -(w[0] * np.asarray(x1, dtype=float) + b) / w[1]

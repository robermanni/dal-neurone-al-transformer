"""Test del Modulo 1. La fixture `impl` (vedi conftest.py) fornisce
esercizi.py con --studente, altrimenti soluzioni.py."""
import numpy as np
import pytest


def dataset_separabile(seed=0):
    rng = np.random.default_rng(seed)
    positivi = rng.normal([2.0, 2.0], 0.5, size=(30, 2))
    negativi = rng.normal([-2.0, -2.0], 0.5, size=(30, 2))
    X = np.vstack([positivi, negativi])
    y = np.array([1] * 30 + [-1] * 30)
    return X, y


XOR_X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
XOR_Y = np.array([-1, 1, 1, -1])


# --- distanza_firmata -------------------------------------------------------

def test_distanza_zero_sul_confine(impl):
    d = impl.distanza_firmata([[0.5, 0.5]], w=[1, 1], b=-1)
    assert np.allclose(d, 0.0)


def test_distanza_ha_valore_e_segno_corretti(impl):
    d = impl.distanza_firmata([[3, 4], [-3, -4]], w=[3, 4], b=0)
    assert np.allclose(d, [5.0, -5.0])


def test_distanza_non_cambia_se_scalo_w_e_b(impl):
    X = [[1.0, 2.0], [-0.5, 3.0]]
    d1 = impl.distanza_firmata(X, w=[1, -2], b=0.5)
    d2 = impl.distanza_firmata(X, w=[10, -20], b=5)
    assert np.allclose(d1, d2)


def test_distanza_con_w_nullo_solleva_errore(impl):
    with pytest.raises(ValueError):
        impl.distanza_firmata([[1, 1]], w=[0, 0], b=1)


# --- margine ----------------------------------------------------------------

def test_margine_positivo_se_tutti_corretti(impl):
    X = [[2, 0], [-1, 0]]
    m = impl.margine(X, [1, -1], w=[1, 0], b=0)
    assert isinstance(m, float)
    assert m == pytest.approx(1.0)


def test_margine_negativo_se_un_punto_e_sbagliato(impl):
    X = [[2, 0], [1, 0]]
    m = impl.margine(X, [1, -1], w=[1, 0], b=0)
    assert m == pytest.approx(-1.0)


# --- addestra_percettrone ---------------------------------------------------

def test_percettrone_separa_dati_separabili(impl):
    X, y = dataset_separabile()
    w, b, errori = impl.addestra_percettrone(X, y)
    assert np.all(y * (X @ w + b) > 0)
    assert errori[-1] == 0


def test_percettrone_si_ferma_appena_converge(impl):
    X, y = dataset_separabile()
    _, _, errori = impl.addestra_percettrone(X, y, max_epoche=100)
    assert len(errori) < 100
    assert all(e > 0 for e in errori[:-1])


def test_percettrone_non_risolve_xor(impl):
    _, _, errori = impl.addestra_percettrone(XOR_X, XOR_Y, max_epoche=50)
    assert len(errori) == 50
    assert min(errori) > 0


def test_percettrone_primo_aggiornamento(impl):
    # Con w = 0 il primo punto è sempre "sbagliato" (punteggio 0)
    w, b, errori = impl.addestra_percettrone([[1.0, 2.0]], [1], max_epoche=5)
    assert np.allclose(w, [1.0, 2.0])
    assert b == pytest.approx(1.0)
    assert errori == [1, 0]


# --- confine_retta ----------------------------------------------------------

def test_confine_retta_punti_a_punteggio_zero(impl):
    w, b = np.array([2.0, -1.0]), 3.0
    x1 = np.linspace(-5, 5, 11)
    x2 = impl.confine_retta(w, b, x1)
    assert np.allclose(w[0] * x1 + w[1] * x2 + b, 0.0)


def test_confine_verticale_solleva_errore(impl):
    with pytest.raises(ValueError):
        impl.confine_retta([1.0, 0.0], 0.0, [0, 1])

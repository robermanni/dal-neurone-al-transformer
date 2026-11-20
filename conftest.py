"""Configurazione comune dei test.

Di default i test verificano le soluzioni di riferimento (soluzioni.py),
così la CI resta verde. Con l'opzione --studente verificano invece il
TUO codice in esercizi.py:

    python -m pytest moduli/01_neurone --studente
"""
import importlib.util
import pathlib

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--studente",
        action="store_true",
        help="Verifica le tue soluzioni in esercizi.py invece di soluzioni.py",
    )


@pytest.fixture
def impl(request):
    """Carica esercizi.py o soluzioni.py dalla cartella del modulo in esame."""
    nome = "esercizi" if request.config.getoption("--studente") else "soluzioni"
    percorso = pathlib.Path(request.path).parent / f"{nome}.py"
    spec = importlib.util.spec_from_file_location(f"{nome}_{percorso.parent.name}", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

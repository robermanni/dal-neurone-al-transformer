# Dal neurone al transformer

[![Test](https://github.com/robermanni/dal-neurone-al-transformer/actions/workflows/tests.yml/badge.svg)](https://github.com/robermanni/dal-neurone-al-transformer/actions/workflows/tests.yml)
[![Licenza: MIT](https://img.shields.io/badge/licenza-MIT-blue.svg)](LICENSE)

**Un percorso in Python per capire come funzionano davvero le reti neurali: dal singolo neurone fino a un piccolo modello linguistico addestrato su testo italiano.**

🇬🇧 *[English version below](#english)*

Gli LLM sembrano magia, ma sono costruiti con pochi mattoni che si possono capire uno alla volta. In questo percorso ogni mattone viene **spiegato, implementato da zero in NumPy e poi confrontato con PyTorch**, con grafici per vedere cosa succede ed esercizi con test automatici per verificare di aver capito.

## Il percorso

| # | Modulo | Cosa costruisci | Stato |
|:-:|---|---|:-:|
| 1 | [Il neurone e il classificatore lineare](moduli/01_neurone/lezione.ipynb) | punteggio, confine di decisione, percettrone, il limite di XOR | ✅ |
| 2 | La discesa del gradiente | funzioni di perdita, gradiente, regressione logistica | 🔜 |
| 3 | Reti a più strati e XOR | strati nascosti, attivazioni non lineari | 🔜 |
| 4 | La backpropagation | derivate a catena scritte a mano, controllo numerico del gradiente | 🔜 |
| 5 | Un mini motore di autograd | come PyTorch calcola i gradienti "sotto il cofano" | 🔜 |
| 6 | Embedding e spazi vettoriali | rappresentare parole come vettori, PCA, t-SNE, UMAP | 🔜 |
| 7 | Il meccanismo di attention | query, key, value e self-attention | 🔜 |
| 8 | Un piccolo GPT in italiano | un transformer addestrato sui *Promessi Sposi* | 🔜 |

## Come si usa ogni modulo

Ogni cartella in `moduli/` contiene:

- `lezione.ipynb` – la lezione: teoria, codice e grafici, da leggere ed eseguire;
- `esercizi.py` – le funzioni da completare tu;
- `test_esercizi.py` – i test che verificano il tuo lavoro;
- `soluzioni.py` – le soluzioni di riferimento (da guardare *dopo* averci provato).

## Per iniziare

**Senza installare nulla:** apri la lezione su Google Colab.
[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robermanni/dal-neurone-al-transformer/blob/main/moduli/01_neurone/lezione.ipynb)

**Sul tuo computer:**

```bash
git clone https://github.com/robermanni/dal-neurone-al-transformer.git
cd dal-neurone-al-transformer
python -m venv .venv && source .venv/bin/activate   # su Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook moduli/01_neurone/lezione.ipynb
```

**Verifica i tuoi esercizi:**

```bash
python -m pytest moduli/01_neurone --studente
```

Senza `--studente` i test verificano le soluzioni di riferimento: è ciò che fa la CI a ogni modifica, insieme all'esecuzione completa di tutti i notebook.

## Prerequisiti

Python di base (funzioni, liste, cicli) e un po' di familiarità con NumPy. La matematica necessaria (vettori, prodotto scalare, derivate) viene richiamata quando serve.

## Ispirazione

Questo percorso deve molto a [micrograd](https://github.com/karpathy/micrograd) e [nanoGPT](https://github.com/karpathy/nanoGPT) di Andrej Karpathy. La differenza sta nell'approccio didattico: lezioni in italiano, attenzione alla geometria e all'intuizione, esercizi verificabili con test automatici.

## Autore

**Roberto Fermanelli** – formatore tecnico su intelligenza artificiale, LLM e Python.
[LinkedIn](https://www.linkedin.com/in/roberto-fermanelli) · Suggerimenti e segnalazioni sono benvenuti nelle [Issues](https://github.com/robermanni/dal-neurone-al-transformer/issues).

---

<a id="english"></a>
## English

**From neuron to transformer** is a hands-on Python course that builds, one piece at a time, every component behind modern language models: from a single neuron to a small GPT trained on Italian text.

Each component is **explained, implemented from scratch in NumPy, then checked against PyTorch**, with visualizations and exercises verified by automated tests. Lessons are written in Italian; code, function names and docstrings follow a consistent structure that is easy to follow with a translator.

**Quick start:** open any lesson in Colab, or clone the repository, run `pip install -r requirements.txt`, and check your solutions with `python -m pytest moduli/01_neurone --studente`.

Inspired by Andrej Karpathy's micrograd and nanoGPT. Released under the MIT License.

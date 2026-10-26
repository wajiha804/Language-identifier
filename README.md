\# Language Identifier



Identifies whether a sentence is English, Hindi, Telugu, Spanish or French, using character n-gram language models built from scratch in Python (no NLP library for the model). Includes a small Flask web app.



\## How it works

\- Each language has a small training text in the `data` folder.

\- Text is cut into overlapping 3-letter chunks (character trigrams), and the program counts how often each chunk appears per language.

\- For a new sentence, it scores every language by how likely its chunks are, using add-one smoothing so unseen chunks don't give a zero score.

\- The language with the highest score wins.



\## Results

Tested on 26 sentences that were not in the training text.



| Chunk size (N) | Correct |

|---|---|

| 1 | 19 / 26 |

| 2 | 24 / 26 |

| 3 | 24 / 26 |

| 4 | 22 / 26 |



N=1,2 and 4 were measured before I added more English training text.



Single letters (N = 1) did clearly worse. N = 2 to 4 were close, and the test set is small, so I don't claim one of them is best.



\## Known limitations

\- Only five languages are supported. Text in other languages gets assigned to the closest of the five.

\- Very short inputs ("hi") can be wrong.

\- Hindi written in English letters ("namaste") is not recognized, because the model only saw Devanagari Hindi.

\- The first English training text had no apostrophes, so "I don't like you" was wrongly labeled French. Adding English text with contractions fixed it.



\## Run it

```

pip install -r requirements.txt

python app.py

```

Then open http://127.0.0.1:5000



\## Files

\- `identifier.py`: the model

\- `tests.py`: accuracy test

\- `app.py`: web page

\- `data/`: training text


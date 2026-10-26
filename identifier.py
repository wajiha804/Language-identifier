import math
from collections import Counter

N = 3 # size of the letter chunks; we'll try 1, 2, 3, 4 later

FILES = {
    "English": "data/en.txt",
    "Hindi":   "data/hi.txt",
    "Telugu":  "data/te.txt",
    "Spanish": "data/es.txt",
    "French":  "data/fr.txt",
}

def get_ngrams(text, n=N):
    text = " ".join(text.lower().split())   # clean spaces and newlines
    text = " " * (n - 1) + text + " "       # padding at the start and end
    return [text[i:i + n] for i in range(len(text) - n + 1)]

# Training: count the letter chunks of each language
models = {}
for lang, path in FILES.items():
    with open(path, encoding="utf-8") as f:
        models[lang] = Counter(get_ngrams(f.read()))

totals = {lang: sum(c.values()) for lang, c in models.items()}
vocab_size = len(set().union(*[set(c) for c in models.values()]))

def score(text, lang):
    """How well does this text fit this language? (higher is better)"""
    total = 0.0
    for g in get_ngrams(text):
        # add-one smoothing: unseen chunks get a small chance, not zero
        p = (models[lang][g] + 1) / (totals[lang] + vocab_size)
        total += math.log(p)
    return total

def detect(text):
    scores = {lang: score(text, lang) for lang in models}
    return max(scores, key=scores.get)

if __name__ == "__main__":
    print(detect("The weather is very nice today"))
    print(detect("नमस्ते, आप कैसे हैं?"))
    print(detect("Hoy hace muy buen tiempo"))
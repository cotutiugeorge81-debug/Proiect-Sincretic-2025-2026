import argparse
import os
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def main():
    parser = argparse.ArgumentParser(description="Analizor de text")
    parser.add_argument("fisier")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--ngrams", type=int, default=1)
    args = parser.parse_args()

    if not os.path.exists(args.fisier): return

    with open(args.fisier, 'r', encoding='utf-8') as f:
        text_brut = f.read()

    tokens = word_tokenize(re.sub(r"[^\w\s]", "", text_brut.lower()))
    
    # Filtram stop-words pentru limba romana
    stop_words = set(stopwords.words('romanian'))
    cuvinte_curate = [w for w in tokens if w not in stop_words]
    
    print(f"Cuvinte dupa filtrare: {len(cuvinte_curate)}")

if __name__ == "__main__":
    main()

import argparse
import os
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Descarcam resursele necesare
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def main():
    parser = argparse.ArgumentParser(description="Analizor de text")
    parser.add_argument("fisier", help="Numele fisierului .txt")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--ngrams", type=int, default=1)
    args = parser.parse_args()

    if not os.path.exists(args.fisier):
        print(f"Eroare: Fisierul '{args.fisier}' nu exista.")
        return

    with open(args.fisier, 'r', encoding='utf-8') as f:
        text_brut = f.read()

    # Curatare si Tokenizare
    tokens = word_tokenize(re.sub(r"[^\w\s]", "", text_brut.lower()))
    
    # Filtrare Stopwords (limba romana)
    stop_words = set(stopwords.words('romanian'))
    cuvinte_curate = [w for w in tokens if w not in stop_words]
    
    # Calcul frecventa
    numaratoare = Counter(cuvinte_curate).most_common(args.top)
    
    print(f"Analiza text: {args.fisier} ({len(tokens)} cuvinte)")
    print(f"Top {args.top} cuvinte (fara stopwords):")
    
    for i, (cuvant, count) in enumerate(numaratoare, 1):
        procent = (count / len(tokens)) * 100
        print(f"{i}. {cuvant} - {count} aparitii ({procent:.2f}%)")

if __name__ == "__main__":
    main()

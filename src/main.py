import argparse
import os
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

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
    stop_words = set(stopwords.words('romanian'))
    cuvinte_curate = [w for w in tokens if w not in stop_words]
    
    lemmatizer = WordNetLemmatizer()
    cuvinte_procesate = [lemmatizer.lemmatize(w) for w in cuvinte_curate]
    
    print(f"Analiza text: {args.fisier} ({len(tokens)} cuvinte)")

    if args.ngrams > 1:
        # Generam n-grame (perechi de cuvinte)
        n_grame = list(nltk.ngrams(cuvinte_procesate, args.ngrams))
        numaratoare = Counter(n_grame).most_common(args.top)
        
        print(f"Top {args.top} {args.ngrams}-grame:")
        for i, (gram, count) in enumerate(numaratoare, 1):
            text_gram = " ".join(gram)
            print(f"{i}. \"{text_gram}\" - {count} aparitii")
    else:
        # Analiza cuvinte individuale
        numaratoare = Counter(cuvinte_procesate).most_common(args.top)
        print(f"Top {args.top} cuvinte (fara stopwords):")
        for i, (cuvant, count) in enumerate(numaratoare, 1):
            procent = (count / len(tokens)) * 100
            print(f"{i}. {cuvant} - {count} aparitii ({procent:.2f}%)")

if __name__ == "__main__":
    main()

import argparse
import os
import re
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

# Resurse necesare NLTK
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

def main():
    parser = argparse.ArgumentParser(description="Analizor de text NLTK")
    parser.add_argument("fisier", help="Numele fisierului .txt")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--ngrams", type=int, default=1)
    parser.add_argument("--diversity", action="store_true")
    parser.add_argument("--concordance", type=str, help="Cauta contextul unui cuvant")
    parser.add_argument("--cloud", action="store_true", help="Afiseaza un nor de cuvinte")
    args = parser.parse_args()

    if not os.path.exists(args.fisier):
        print(f"Eroare: Fisierul '{args.fisier}' nu exista.")
        return

    with open(args.fisier, 'r', encoding='utf-8') as f:
        text_brut = f.read()

    # Preprocesare
    tokens_totali = word_tokenize(re.sub(r"[^\w\s]", "", text_brut.lower()))
    stop_words = set(stopwords.words('romanian'))
    lemmatizer = WordNetLemmatizer()
    
    cuvinte_curate = [lemmatizer.lemmatize(w) for w in tokens_totali if w not in stop_words and len(w) > 2]

    # 1. DIVERSITATE (--diversity)
    if args.diversity:
        cuvinte_unice = set(cuvinte_curate)
        ttr = len(cuvinte_unice) / len(tokens_totali)
        print(f"Diversitate vocabular:\nTotal cuvinte: {len(tokens_totali)}")
        print(f"Cuvinte unice: {len(cuvinte_unice)} ({len(cuvinte_unice)/len(tokens_totali)*100:.1f}%)")
        print(f"Type-Token Ratio: {ttr:.3f}")
        return

    # 2. CONCORDANTA (--concordance "cuvant")
    if args.concordance:
        print(f"Concordanta pentru \"{args.concordance}\":")
        text_nltk = nltk.Text(word_tokenize(text_brut.lower()))
        conlines = text_nltk.concordance_list(args.concordance, width=60, lines=5)
        for i, line in enumerate(conlines, 1):
            print(f"{i}. ...{line.line}...")
        return

    # 3. CLOUD (--cloud)
    if args.cloud:
        top_cloud = Counter(cuvinte_curate).most_common(20)
        random.shuffle(top_cloud)
        print("--- Word Cloud (Terminal) ---")
        for i in range(0, len(top_cloud), 4):
            rand = top_cloud[i:i+4]
            linie = "  ".join([c.upper() if n > 5 else c for c, n in rand])
            print(linie)
        return

    # 4. ANALIZA STANDARD (Unigrame/N-grame)
    print(f"Analiza text: {args.fisier} ({len(tokens_totali)} cuvinte)")
    if args.ngrams > 1:
        n_grame = list(nltk.ngrams(cuvinte_curate, args.ngrams))
        numaratoare = Counter(n_grame).most_common(args.top)
        print(f"Top {args.top} {args.ngrams}-grame:")
        for i, (gram, count) in enumerate(numaratoare, 1):
            print(f"{i}. \"{' '.join(gram)}\" - {count} aparitii")
    else:
        numaratoare = Counter(cuvinte_curate).most_common(args.top)
        print(f"Top {args.top} cuvinte (fara stopwords):")
        for i, (cuvant, count) in enumerate(numaratoare, 1):
            procent = (count / len(tokens_totali)) * 100
            print(f"{i}. {cuvant} - {count} aparitii ({procent:.2f}%)")

if __name__ == "__main__":
    main()

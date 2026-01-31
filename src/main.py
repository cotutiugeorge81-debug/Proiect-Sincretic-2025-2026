import argparse
import os
import re
import nltk
from nltk.tokenize import word_tokenize

# Descarcam resursele minime necesare
nltk.download('punkt', quiet=True)

def main():
    parser = argparse.ArgumentParser(description="Analizor de text")
    parser.add_argument("fisier")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--ngrams", type=int, default=1)
    args = parser.parse_args()

    if not os.path.exists(args.fisier):
        print("Eroare: Fisier negasit.")
        return

    with open(args.fisier, 'r', encoding='utf-8') as f:
        text_brut = f.read()

    # Curatam textul de semne de punctuatie si facem litere mici
    text_curat = re.sub(r"[^\w\s]", "", text_brut.lower())
    
    # Transformam textul in lista de cuvinte (tokeni)
    tokens = word_tokenize(text_curat)
    
    print(f"Analiza text: {args.fisier} ({len(tokens)} cuvinte)")

if __name__ == "__main__":
    main()

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Analizor de text")
    parser.add_argument("fisier", help="Numele fisierului")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--ngrams", type=int, default=1)
    
    args = parser.parse_args()

    # Verificam daca fisierul exista pe disc
    if not os.path.exists(args.fisier):
        print(f"Eroare: Fisierul '{args.fisier}' nu a fost gasit.")
        return

    # Citim continutul fisierului
    with open(args.fisier, 'r', encoding='utf-8') as f:
        text_brut = f.read()
    
    print(f"Succes! Am citit fisierul. Lungime text: {len(text_brut)} caractere.")

if __name__ == "__main__":
    main()

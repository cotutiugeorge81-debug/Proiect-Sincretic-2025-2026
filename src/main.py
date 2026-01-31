import argparse

def main():
    parser = argparse.ArgumentParser(description="Analizor de text")
    parser.add_argument("fisier", help="Numele fisierului")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--ngrams", type=int, default=1)
    
    args = parser.parse_args()
    print("Programul a pornit pentru fisierul:", args.fisier)

if __name__ == "__main__":
    main()

Word Analyzer NLTK
Aplicație avansată pentru analiza lingvistică a textelor în limba română.
Permite extragerea frecvențelor, analiza n-gramelor, calculul diversității lexicale și vizualizarea contextului cuvintelor.

Nume: Cotutiu Ionut-George

Descriere
Aplicația rezolvă problema procesării rapide a volumelor mari de text, oferind statistici relevante pentru lingviști sau cercetători.
Aceasta curăță textul automat, elimină cuvintele de legătură (stopwords) și normalizează cuvintele prin lemmatizare pentru a oferi rezultate precise.

Tehnologii folosite
Limbaj: Python 3.10
Biblioteci:

nltk - Procesarea limbajului natural (tokenizare, lemmatizare, n-grame)

argparse - Gestionarea interfeței în linie de comandă

collections.Counter - Numărarea eficientă a frecvențelor


Instalare & Rulare (Fără Docker)
# Instalare dependinte
pip install nltk
# Rulare
python src/main.py data/discurs.txt --top 5

Rulare (Cu Docker)
# Build imagine
docker build -t word-analyzer-upt .
# Rulare
docker run word-analyzer-upt data/discurs.txt --diversity

Exemple de utilizare
Analiză Top Cuvinte: python src/main.py data/discurs.txt --top 10 (afișează frecvența și procentajul)

Analiză Bigrame: python src/main.py data/discurs.txt --ngrams 2 --top 5

Statistici Diversitate: python src/main.py data/discurs.txt --diversity

Căutare în Context: python src/main.py data/discurs.txt --concordance "educație"

Vizualizare Cloud: python src/main.py data/discurs.txt --cloud


Structura proiectului
word-analyzer-upt/

├── .github/workflows/build.yml - CI/CD pipeline

├── src/

│   └── main.py - Scriptul principal de analiză

├── data/

│   └── discurs.txt - Fișier text pentru testare

├── Dockerfile - Configurația pentru containerizare

└── README.md - Documentația curentă

Probleme întâlnite și soluții

Problemă: Eroare OSError la încărcarea dicționarelor de stopwords.

Soluție: Am corectat typo-ul din cod și am adăugat instrucțiunile nltk.download automate în main.py și Dockerfile.

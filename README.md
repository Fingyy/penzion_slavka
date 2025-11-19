# Penzion Slávka
Webová stránka penzionu, se základními informacemi o nabídce ubytování, zajímavých míst v okolí a možností poptání ubytování pomocí jednoduchého formuláře. 

## Požadavky
- python~= 3.7
- django~=3.2.25
- requests~=2.31.0

## Použité technologie
- Django, Python
- HTML, CSS

## Setup
### 1. Klonování repozitáře:
```
git clone https://github.com/Fingyy/penzion_slavka.git
```
### 2. Vytvoření a nastavení virtual env:
Windows
```
pip install virtualenv
python -m virtualenv venv
.\venv\Scripts\activate
```
Mac
```
pip install virtualenv
python -m virtualenv venv
source venv/bin/activate
```
### 3. Instalace závislostí:
```
pip install -r requirements.txt
```
### 4. Nastavení databáze:
```
python manage.py migrate
```
### 5. Spuštění serveru:
```
python manage.py runserver
```
### 6. Přístup k aplikaci:
- Otevřete webový prohlížeč a přejděte na http://localhost:8000/
- Pro administrativní rozhraní přejděte na http://localhost:8000/admin/

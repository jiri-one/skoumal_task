# Authors & Websites Django API

Demo backend s Django REST Framework pro autory a jejich weby.

## Endpoints

- `POST /author` — vytvoří autora (`name`, `age`, `email`, `phonenumber`)
- `GET /author` — vypíše autory včetně jejich webů
- `POST /website` — vytvoří web pro autora (`name`, `url`, `author`)

## Rychlý start

1. **Naklonuj repo** a nainstaluj závislosti:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install django djangorestframework
   ```

2. **Inicializuj databázi:**
   ```bash
   python manage.py migrate
   ```

3. **Spusť testy (volitelné):**
   
   Pro spuštění testů je nutné nainstalovat pytest
   ```bash
   pip install pytest-django
   ```
   pak už půjdou spustit samotné testy:
   ```bash
   pytest -v
   ```

4. **Spusť server:**
   ```bash
   python manage.py runserver
   ```

5. **Vyzkoušej API:**
   - POST `/author` (JSON): `{ "name": "Tom", "age": 30, "email": "tom@x.cz", "phonenumber": "+420123456789" }`
   - POST `/website` (JSON): `{ "name": "TomSite", "url": "https://tom.cz", "author": 1 }`
   - GET `/author`

## Poznámky

- Pro demo je použito SQLite, ale pokud si nakonfigurujete jinou DB, tak to bude fungovat také.

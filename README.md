# django_start

Materiał 10 – Django, start. Projekt `config`, aplikacja `shop`.

## Uruchomienie

```powershell
python --version                 # wymagane 3.12+
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
django-admin --version           # powinno być 6.x
python manage.py runserver
```

Serwer: http://127.0.0.1:8000

## Obserwacje

### Zadanie 4 – ukośnik na końcu

`/about` (bez ukośnika) zwraca **301** i przekierowuje na `/about/`, który zwraca **200** (w Network są dwa żądania; robi to `CommonMiddleware` przez `APPEND_SLASH`). Po zmianie wzorca na `"about"` działa `/about` (200), a `/about/` daje 404 – wzorzec musi pasować dokładnie.

### Zadanie 5 – `/add/a/b/`

Zwraca **404**. Konwerter `<int:a>` nie dopasowuje liter, więc żaden wzorzec nie pasuje do adresu i Django nie wywołuje widoku w ogóle. `/divide/7/0/` zwraca 400 (błąd klienta, obsłużony w widoku).

### Zadanie 6 – slug

`/products/laptop-dell-15/` działa (200) – slug to litery, cyfry, `-` i `_`. `/products/laptop dell/` (spacja jest kodowana jako `%20`) daje 404, bo spacja nie należy do znaków dozwolonych w slugu, więc wzorzec nie pasuje.

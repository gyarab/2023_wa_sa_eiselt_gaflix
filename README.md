# Lepsi Netflix ofc


## Co je potreba dodelat

```
predelat databazi hercu a dpolnit je vsude
zmeni IDcka u vsech
dodelat frontend
```

## První inicializace projektu

```
git clone https://github.com/gyarab/2023_wa_sa_eiselt_gaflix.git
cd 2023_wa_sa_eiselt_gaflix/

py -3 -m venv venv
source ./venv/Scripts/activate

pip install -r requirements.txt
```

```
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

## Spuštění projektu

```
git pull
source ./venv/Scripts/activate
./manage.py migrate
./manage.py runserver
```

## Po změně `models.py`

```
./manage.py makemigrations
./manage.py migrate
```

```
export PYTHONIOENCODING=utf-8 && python manage.py dumpdata --indent 2 movies.director > fixtures/directors.json
```
```
 python manage.py loaddata fixtures/*.json
```

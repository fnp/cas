O projekcie
-----------

CAS to aplikacja WWW służąca do uwierzytelniania użytkowników 
serwisów Fundacji Nowoczesna Polska. Implementuje ona protokół CAS <http://www.jasig.org/cas>
w  wersjach 1.0 i 2.0.

Wymagania
---------

* Zobacz requirements.txt

Instalacja i uruchomienie
-------------------------

1. Zainstaluj wymagane biblioteki, np. używając pip:

    pip install -r requirements.txt

2. Wypełnij bazę danych (Django poprosi o utworzenie pierwszego użytkownika)

	./manage.py syncdb --migrate
	
5. Uruchom serwer deweloperski

	./manage.py runserver

6. Przy wdrożeniu utwórz plik `localsettings.py` i wpisz tam 
ustawienia używanej bazy danych.

O projekcie
-----------

CAS to aplikacja WWW służąca do uwierzytelniania (a w przyszłości również autoryzacji) użytkowników 
serwisów Fundacji Nowoczesna Polska. Implementuje on protokół CAS <http://www.jasig.org/cas> w 
wersji 1.0.

Wymagania
---------

* Django 1.1 <http://djangoproject.com/>
* zuber/django-cas-provider <http://github.com/zuber/django-cas-provider>

Instalacja i uruchomienie
-------------------------

1. Ściągnij i zainstaluj pip <http://pypi.python.org/pypi/pip>
2. Przejdź do katalogu aplikacji w konsoli
3. Zainstaluj wymagane biblioteki (patrz sekcja wymagania_) komendą

    pip install -r requirements.txt

4. Wypełnij bazę danych (Django poprosi o utworzenie pierwszego użytkownika)

	./manage.py syncdb
	
5. Uruchom serwer deweloperski

	./manage.py runserver

6. Przy wdrożeniu będziesz musiał najpewniej utworzyć plik `localsettings.py` i wpisać tam 
ustawienia używanej bazy danych. Zalecane jest serwowanie aplikacji przez modwsgi na serwerze Apache2.
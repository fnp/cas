================================
Fundacja Nowoczesna Polska - CAS
================================

O projekcie
===========
CAS to aplikacja WWW służąca do autentykacji (a w przyszłości również autoryzacji) użytkowników 
serwisów Fundacji Nowoczesna Polska. Implementuje on protokół `CAS <http://www.jasig.org/cas>`_ w 
wersji 1.0.

Wymagania
=========
* `Django 1.1 <http://djangoproject.com/>`_
* `zuber/django-cas-provider <http://github.com/zuber/django-cas-provider>`_

Instalacja i uruchomienie
=========================
1. Ściągnij i zainstaluj `pip <http://pypi.python.org/pypi/pip>`_
2. Przejdź do katalogu aplikacji w konsoli
3. Zainstaluj wymagane biblioteki (patrz sekcja wymagania_) komendą::

	pip install -r requirements.txt

4. Wypełnij bazę danych (Django poprosi o utworzenie pierwszego użytkownika)::

	./manage.py syncdb
	
5. Uruchom serwer deweloperski::

	./manage.py runserver

6. Przy wdrożeniu będziesz musiał najpewniej utworzyć plik `localsettings.py` i wpisać tam 
ustawienia używanej bazy danych. Zalecane jest serwowanie aplikacji 
przez `modwsgi <http://code.google.com/p/modwsgi/>`_ na serwerze `Apache2 <http://httpd.apache.org/>`_ 
przy pomocy załączonego skryptu `dispatch.fcgi`. Inne strategie wdrożeniowe opisane 
są w `Dokumentacji Django <http://docs.djangoproject.com/en/dev/howto/deployment/#howto-deployment-index>`_.
.PHONY: deploy

UID != id -u
GID != id -g

deploy: src/cas/localsettings.py
	pip install -r requirements.txt
	src/manage.py migrate --noinput
	src/manage.py collectstatic --noinput


test:
	rm -r htmlcov &
	docker-compose run --rm dev sh -c '\
		coverage run --branch --source='.' --data-file ../.coverage ./manage.py test; \
		coverage html --data-file ../.coverage -d htmlcov; \
		coverage report --data-file ../.coverage; \
		chown -R $(UID):$(GID) htmlcov'
	mv -f src/htmlcov .


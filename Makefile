fixture: 
	python manage.py loaddata core/fixtures/profiles.yaml
	python manage.py loaddata core/fixtures/jobs.yaml

install: 
	pip install -r requirements.txt
	python manage.py migrate
	make fixture

run:
	python manage.py runserver
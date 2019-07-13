dev:
	docker-compose build webapp
	docker-compose up webapp
build:
	docker build . -t kevin91nl/citextract
push:
	docker push kevin91nl/citextract
check:
	flake8
	find . -iname "*.py" ! -wholename "*node_modules*" ! -wholename "*migrations*" ! -wholename "*.git*" ! -wholename "*test_data*" ! -wholename "*tests*" ! -wholename "*manage.py*" ! -wholename "*sandbox*" | xargs pylint
	pydocstyle --convention=numpy --match-dir "^(?!migrations|node_modules|\.git|test_data|tests|sandbox).*"
	python manage.py test
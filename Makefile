.PHONY: run build black
# ensure cpython is not generated
run:
	poetry install
	poetry run python -B index.py

black:
	poetry run black ./

lint:
	poetry run flake8 --ignore=E501,W503 ./src
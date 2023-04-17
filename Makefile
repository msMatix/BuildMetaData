.PHONY: run
run:
	python3 -m "BuildMetaData.main"

.PHONY: test
test:
	python3 -m pytest -s tests/

.PHONY: cov
cov:
	python3 -m pytest tests/ --cov-report term-missing:skip-covered --cov-config pytest.ini --cov=. tests/ -vv

.PHONY: env
env:
	poetry shell

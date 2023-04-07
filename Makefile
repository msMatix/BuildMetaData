.PHONY: run
run:
	python3 -m "BuildMetaData.main"

.PHONY: env
env:
	poetry shell

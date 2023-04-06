.PHONY: run
run:
	# textual run "calculator.app:CalculatorApp"

.PHONY: dev
dev:
	# while true; do textual run --dev "calculator.app:CalculatorApp"; done

.PHONY: debug
debug:
	# textual console

.PHONY: env
env:
	poetry shell

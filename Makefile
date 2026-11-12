PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) secret_scanner.py sample_backup.log

.PHONY: replay
replay:
	$(PYTHON) tools/replay_examples.py --report reports/replay.md

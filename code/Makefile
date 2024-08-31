# Manages building, testing, and cleaning the code as well as running the code
# to generate the results and figures for the paper.

PACKAGE_NAME = sqic
TEST_DIR = tests


.PHONY: all
#
all: build test

.PHONY: clean
# Remove all processing artifacts, build files and cache files
clean:
	find . -name "*.pyc" -exec rm -v {} \;
	rm -rf .ruff_cache/ .pytest_cache/
	rm -rvf build dist MANIFEST *.egg-info __pycache__ .coverage .cache

.PHONY: build
# Build `sqic` package and install in the local environment
build:
	pip install --no-deps -e .

.PHONY: check-tools
# Check if code styling and static analysis tools are available in the environment
check-tools:
	@which black >/dev/null || (echo "'black' is not found in the environment. Install it with 'pip install black' command." && exit 1)
	@which ruff >/dev/null || (echo "'ruff' is not found in the environment. Install it with 'pip install ruff' command." && exit 1)

.PHONY: lint
# Check source code for style compliance and run static analysis
lint: check-tools
	black --diff --check $(PACKAGE_NAME) $(TEST_DIR) setup.py -q
	ruff check $(PACKAGE_NAME) setup.py

.PHONY: format
# Format source code and fix static analysis errors
format: check-tools
	black $(PACKAGE_NAME) $(TEST_DIR) setup.py -q
	ruff check --fix $(PACKAGE_NAME) setup.py

.PHONY: test
# Run the test suite
test: check-tools
	@which pytest >/dev/null || (echo "'ruff' is not found in the environment. Install it with 'pip install pytest' command." && exit 1)

	pytest $(TEST_DIR)

.PHONY: coverage
# Calculate test coverage
coverage:
	pytest $(PYTEST_COV_ARGS) --cov=$(PACKAGE) $(PYTEST_ARGS) $(PACKAGE) $(TESTDIR)

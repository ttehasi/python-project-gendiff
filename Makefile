lint:
	ruff check gendiff

install:
	uv sync

build:
	uv build

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

package-install:
	uv tool dist/*.whl

test:
	uv run pytest

check: test lint

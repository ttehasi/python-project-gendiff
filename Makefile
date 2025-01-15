lint:
	ruff check gendiff

install:
	uv sync

build:
	uv build

package-install:
	uv tool dist/*.whl

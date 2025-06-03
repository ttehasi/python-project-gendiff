### Hexlet tests and linter status:

[![Actions Status](https://github.com/ttehasi/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ttehasi/python-project-50/actions)
[![Actions Status](https://github.com/ttehasi/python-project-50/actions/workflows/Test-Coverage.yml/badge.svg)](https://github.com/ttehasi/python-project-50/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/88675eaf4e4ca1e04a88/test_coverage)](https://codeclimate.com/github/ttehasi/python-project-50/test_coverage)
## What is this?
#### Gendiff - это консольная утилита для нахождения разницы между двумя файлами расширения yaml или json. Ниже показаны и описаны примеры использования данной консольной утилиты в разных режимах работы.


### Setup

```bash
make install
```


### Run tests

```bash
make test
```
## Режимы работы
### Режим по умолчанию
#### Режим по умолчанию(то есть без опций) выводит результат в отформатированном виде, где наглядно видно, что добавилось(+), что удалилось(-), а что не изменилось(ничего).
### Asciinema JSON file (default usage):
[![asciicast](https://asciinema.org/a/djCfDR2K0qTnGeiqy4hVWhLO9.svg)](https://asciinema.org/a/djCfDR2K0qTnGeiqy4hVWhLO9)

[![asciicast](https://asciinema.org/a/mkiLw1Llc4brT2wrSHaMW7H4T.svg)](https://asciinema.org/a/mkiLw1Llc4brT2wrSHaMW7H4T)

### Asciinema YAML file (default usage):

[![asciicast](https://asciinema.org/a/H918cvPLQohe9DMY2NDxLKcaU.svg)](https://asciinema.org/a/H918cvPLQohe9DMY2NDxLKcaU)

[![asciicast](https://asciinema.org/a/eqSYOXkzxMhXXDIPTiRrzoWmN.svg)](https://asciinema.org/a/eqSYOXkzxMhXXDIPTiRrzoWmN)
### Режим plain 
#### Чтобы использовать plain формат используйте:
```bash
gendiff --format plain path1 path2
```
#### Такое использование выводит результат в виде плоского текста где все изменения описываются словами.
## Asciinema JSON file (plain format name):

[![asciicast](https://asciinema.org/a/VJBLone0FBZy3MkXrEJxVVswy.svg)](https://asciinema.org/a/VJBLone0FBZy3MkXrEJxVVswy)

## Asciinema YAML file (plain format name):

[![asciicast](https://asciinema.org/a/Rfrx6rnCFN0Bv6gBXtXo4ilZG.svg)](https://asciinema.org/a/Rfrx6rnCFN0Bv6gBXtXo4ilZG)
### Режим json 
#### Чтобы использовать json формат используйте:
```bash
gendiff --format json path1 path2
```
#### Такое использование выводит результат, отформатированный по правилам строения json-файлов, может использоваться для обмена между приложениями через api.
## Asciinema JSON file (json format name):

[![asciicast](https://asciinema.org/a/4I6mEhSQg3cpc7PTGsdX9tbxm.svg)](https://asciinema.org/a/4I6mEhSQg3cpc7PTGsdX9tbxm)

## Asciinema YAML file (json format name):

[![asciicast](https://asciinema.org/a/jl5IqTYh5vxNpixkSOtzUIfaW.svg)](https://asciinema.org/a/jl5IqTYh5vxNpixkSOtzUIfaW)

### Links

This project was built using these tools:

| Tool                                       | Description                                                            |
|--------------------------------------------|------------------------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)           | "An extremely fast Python package and project manager, written in Rust" |
| [Pytest](https://pytest.org)               | "A mature full-featured Python testing tool"                           |
| [ruff](https://docs.astral.sh/ruff/)       | "An extremely fast Python linter and code formatter, written in Rust"  |
| [PyYAML](https://pypi.org/project/PyYAML/) | "YAML file parsing"                                                    |


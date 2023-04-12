## Project Euler Solutions

These are my solutions to the problems on https://projecteuler.net

## Usage

All of the problems may be run via the command line like so:

```
# using the default value provided in the example
python p1.py

# or with a specified parameter appropriate for the context of the problem
python p1.py 1000
```

There are also automated tests to ensure everything is still working.
```
# from project root
# may need to install pytest
pytest

# Have to run specific test through python interpreter for python reasons
python -m pytest tests/test_p1.py
```
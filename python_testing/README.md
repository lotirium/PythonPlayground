# Python Testing Project

## Introduction
This Python testing project showcases unit testing with a simple function `do_stuff` in `main.py`, tested using `unittest` in `test.py` and `test2.py`.

## Project Structure

- `main.py`: Contains the `do_stuff` function for basic arithmetic operations and error handling.
- `test.py` & `test2.py`: These files include unit tests for the `do_stuff` function.
- `__pycache__`: A directory for Python's compiled bytecode files.

## Running the Tests

### Individual Test Files
Run each test file separately using Python:
```bash
python test.py
python test2.py
```

### Running All Tests
To run all test files at once, use the following command in the directory containing your test files:
```bash
python -m unittest discover -v
```
This command searches for all test files in the current directory and subdirectories, running them in verbose mode (`-v`) for detailed output.


## Note
This project is intended for educational purposes, focusing on basic unit testing practices in Python.
```

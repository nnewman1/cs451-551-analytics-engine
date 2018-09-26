# cs 451/551: Simple Analytics Assignment

## Project DUE in repository by Monday Oct 1 by 11:59pm

## Project Description
A small application is needed to perform simple analytics on a small database of anoymous student grades for an anonymous course over many semesters. The database contains a listing of student tuples where each tuple indicates semester course taken, gender, midterm grade, and final grade. The analytics application needs to provide the following kinds of reports:

a. Average grade over the entire database

b. Average change in grade from midterm to final

c. A count of each grade (E.g., #A's, #B's, etc.)

d. Total number of female students

e. Total number of male students

The application can run in the terminal. The database file is JSON encoded and can be opened and loaded using:

```python
data = []
with open('datafile.json') as f:
    data = json.loads(f.read())
```

## Getting Started

1. Fork this project to your repository.
2. Clone **your fork** to your computer.
3. Complete the development tasks listed below then commit and push your changes back up to your GitHub repo.

## Development Tasks

1. Design the application using single class that models an Analytic Engine that contains both data and related methods. This class should also run main().

2. Write unit tests for your class methods using ```unittest``` package.

3. Write documentation for each one of your class methods and generate the html docs with [pydoc](https://docs.python.org/3/library/pydoc.html). Also see [PEP manual on docstrings](https://www.python.org/dev/peps/pep-0257/).

4. Submit entire application project to your github repository. Repo must include your python source file, database file, unit test file, and generated documentation in html. Please use the following directory structure.

```
PROJECT_ROOT
    src/
    docs/
    data/
```


# iHate
An experiment about search engine censorship

## About
This script queries the search suggestions of multiple search engines
for offensive search terms. Ex: I hate "ethnicity". It then displays
the search engines which return search suggestions for the specified
query.

## Prerequisites
* python3
* lxml
* requests
```
$ pip install -r requirements.txt
```

## Usage
```
$ ./ihate.py
or
$ ./ihate.py something
```

## Notes:
I think Google censors "I hate 'name'" in general.

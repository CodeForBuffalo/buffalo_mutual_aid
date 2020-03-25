# Buffalo Mutual Aid Network
![GitHub release (latest by date)](https://img.shields.io/github/v/release/CodeForBuffalo/buffalo_mutual_aid?include_prereleases)
[![Build Status](https://travis-ci.com/CodeForBuffalo/buffalomutualaid.svg?branch=master)](https://travis-ci.com/CodeForBuffalo/buffalomutualaid)
![GitHub](https://img.shields.io/github/license/CodeForBuffalo/buffalo_mutual_aid)


[Buffalo Mutual Aid Network](https://www.facebook.com/groups/740052889874229/about/) is a social action group for peer-to-peer organizing, humanitarian assistance, and reliable information sharing developed in response to the COVID-19 crisis.

## Web Development

### Requirements
Make sure these are installed on your machine.
- [Python](https://www.python.org/downloads/release/python-374/) (3.7+)

#### Clone repository and open terminal in project's root directory.
```
$ PATH\TO\REPO\buffalomutualaid>
```

#### Set up environment 
1. Install [pipenv](https://github.com/pypa/pipenv) to manage Python virtual environment and dependencies. [Learn more about pipenv.](https://realpython.com/pipenv-guide/)

```
pip install pipenv
```

2. Use pipenv to create a Python virtual environment and install dependencies based on the Pipfile.lock
```
pipenv sync
```

#### Start local server
```
pipenv run manage.py runserver
```

#### Visit local server
Open server in browser at [http://localhost:8000/](http://localhost:8000/)

## License

The project is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

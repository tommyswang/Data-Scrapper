Development Guide
===

Below is an explanation of file structure of this project:

* `models`: data models, mostly persisted in the database.
* `controllers`: controller files, defining HTTP request handlers
* `templates`: frontend HTML templates.
* `lib`: shared python classes
    * `lib/parsers`: the parser classes
* `static`: static frontend resources, e.g. Javascript, CSS
* `tests`: unit tests

If you use third-party libraries (such as tabula-py, camelot), please remember to add them to the `requirements.txt` file with the version number.


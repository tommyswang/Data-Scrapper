Development Guide
===

Below is a file structure of this project:

```
├── lib
│   ├── __init__.py
│   └── parsers
│       ├── __init__.py
│       └── demo_parser.py
├── main.py
├── requirements.txt
├── static
│   ├── README.md
│   ├── css
│   ├── files
│   ├── images
│   └── js
├── templates
│   └── index.html
├── tests
│   └── test_paths.py
```

Here is an explanation

* For our parsers, create separate Python files in the `lib/parsers` folder. The Python file should contain a Class. Please refer to `demo_parser.py` as an example.
* For importing customized Python classes in the main app, check how the usage of `DemoParser` in `main.py` file.
* For frontend HTML templates, please put [Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/) HTML template in the `templates`. Please don't change the folder name. It is used by the Flask framework.
* For static files, please put them in the `static` folder under corresponding subfolders.

If you use third-party libraries (such as tabula-py, camelot), please remember to add them to the `requirements.txt` file with the version number.


#The empty setup.py file in tests folder enables us to run pytest command directly in our root directory
import os

os.environ['ENV'] = "testing"

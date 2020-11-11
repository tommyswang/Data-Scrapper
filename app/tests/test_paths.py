import pytest
import requests

from setup import create_app

def get_page(path):
    page = requests.get(path)
    return page


def test_homepage():
    app = create_app(testing=True)
    with app.test_client() as c:
        resp = c.get("/")
        assert resp.status_code == 200

def test_get_form():
    app = create_app(testing=True)
    with app.test_client() as c:
        resp = c.get("/form")
        assert resp.status_code == 200

def test_get_api():
    app = create_app(testing=True)
    with app.test_client() as c:
        resp = c.get("/api")
        assert resp.status_code == 200


def test_get_html():
    app = create_app(testing=True)
    with app.test_client() as c:
        resp = c.get("/html")
        assert resp.status_code == 200


def test_get_pdf():
    app = create_app(testing=True)
    with app.test_client() as c:
        resp = c.get("/pdf")
        assert resp.status_code == 200


def test_list_jobs():
    app = create_app(testing=True)
    with app.test_client() as c:
        resp = c.get("/jobs")
        assert resp.status_code == 200

import pytest
import requests

def get_page(path):
    page = requests.get(path)
    return page

def test_form_response():
    path = "http://localhost:5000/form"
    response = get_page(path)
    assert response.status_code == 200

def test_api_response():
    path = "http://localhost:5000/api"
    response = get_page(path)
    assert response.status_code == 200

def test_html_response():
    path = "http://localhost:5000/html"
    response = get_page(path)
    assert response.status_code == 200

def test_pdf_response():
    path = "http://localhost:5000/pdf"
    response = get_page(path)
    assert response.status_code == 200
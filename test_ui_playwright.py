# test_ui_playwright.py
from playwright.sync_api import sync_playwright

URL_LOGIN = "http://127.0.0.1:5000/login"

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL_LOGIN)
        page.fill('input[name="username"]', "admin")
        page.fill('input[name="password"]', "pass")
        page.click('button[type="submit"]')
        assert "Logged in" in page.content()
        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL_LOGIN)
        page.fill('input[name="username"]', "wronguser")
        page.fill('input[name="password"]', "wrongpass")
        page.click('button[type="submit"]')
        assert "Invalid credentials" in page.content()
        browser.close()


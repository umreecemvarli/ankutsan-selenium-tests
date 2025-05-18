from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import pytest
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_ana_sayfa_yukleniyor_mu(browser):
    try:
        browser.get("https://www.ankutsan.com")
        time.sleep(2)  # Sayfa yüklenmesi için bekleyelim
        assert "Ankutsan" in browser.title
    except WebDriverException as e:
        pytest.fail(f"Siteye erişilemedi: {e}")


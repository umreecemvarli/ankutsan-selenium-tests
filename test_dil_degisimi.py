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

def test_dil_degisimi_ankutsan(browser):
    try:
        browser.get("https://www.ankutsan.com")
        time.sleep(3)

        # Dil seçici: 'TR' yazan bölgeye tıkla
        dil_butonu = browser.find_element(By.CSS_SELECTOR, ".header-top__language__text")
        dil_butonu.click()
        time.sleep(1)

        # EN seçeneğine tıkla (href /en olan link)
        english_option = browser.find_element(By.XPATH, "//a[contains(@href, '/en')]")
        english_option.click()
        time.sleep(3)

        # İngilizce sayfada olduğunu doğrula
        body_text = browser.find_element(By.TAG_NAME, "body").text
        assert "Corporate" in body_text or "About Us" in body_text, "Sayfa İngilizce değil"

    except WebDriverException as e:
        pytest.fail(f"Dil değişikliği testi başarısız: {e}")

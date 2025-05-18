from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_kurumsal_sayfasi(browser):
    try:
        browser.get("https://www.ankutsan.com")

        wait = WebDriverWait(browser, 10)  # 10 saniyeye kadar bekle

        # "Kurumsal" linki tıklanabilir olana kadar bekle
        kurumsal_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Kurumsal")))
        kurumsal_menu.click()

        # Sayfanın "Kurumsal" ifadesini içerdiğini kontrol et
        wait.until(lambda d: "Kurumsal" in d.title or "Kurumsal" in d.page_source)

        assert "Kurumsal" in browser.title or "Kurumsal" in browser.page_source

    except (WebDriverException, NoSuchElementException) as e:
        pytest.fail(f"Kurumsal sayfası açılırken hata oluştu: {e}")

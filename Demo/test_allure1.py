from selenium import webdriver
import allure
from webdriver_manager.chrome import ChromeDriverManager


def test_amazon():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.in")
    print(driver.title)
    assert True
    allure.attach(driver.get_screenshot_as_png(), name='page1.png')
    
    driver.close()
    
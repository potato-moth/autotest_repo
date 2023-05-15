import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome('D:\\PycharmProjects\\autotest_repo\\driver\\chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.quit()

from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    #Form Fields

    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT = (By.XPATH, "//button[@class='btn btn-primary']")
    SUBMIT_ID = (By.ID, "submit")

    #Created data

    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_login_form():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    time.sleep(1)

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(1)

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_add_product():
    backpack_field = driver.find_element(By.XPATH, '//div[normalize-space()="Sauce Labs Backpack"]')
    backpack_field.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
    time.sleep(1)

    Add_to_cart_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    Add_to_cart_button.click()
    time.sleep(1)

    shopping_cart_field = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart_field.click()

    assert driver.current_url == "https://www.saucedemo.com/cart.html"
    time.sleep(1)


# def test_delete_product():
#     remove_button = driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
#     remove_button.click()


def test_checkout():
    checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
    checkout_button.click()

    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
    time.sleep(1)


def test_checkout_log_in():
    First_Name_field = driver.find_element(By.XPATH, '//input[@id="first-name"]')
    First_Name_field.send_keys("Don")
    time.sleep(1)

    Last_Name_field = driver.find_element(By.XPATH, '//input[@id="last-name"]')
    Last_Name_field.send_keys("Smith")
    time.sleep(1)

    Zip_Postal_Code_field = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
    Zip_Postal_Code_field.send_keys("95255")
    time.sleep(1)


def test_continue_checkout():
    continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
    continue_button.click()

    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
    time.sleep(1)


def test_finish_checkout():
    finish_button = driver.find_element(By.XPATH, '//button[@id="finish"]')
    finish_button.click()

    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"

    driver.quit()

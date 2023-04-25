from behave import *
import time


# scenario #1 - Admin login
@given('user enters valid login information') 
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8090/administration')
    text_area = context.driver.find_element("xpath", '//*[@id="input-username"]')
    text_area.send_keys("user")
    text_area = context.driver.find_element("xpath", '//*[@id="input-password"]')
    text_area.send_keys("bitnami")

@when('user clicks on "Login"')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="form-login"]/div[3]/button').click()

@then('user is successfully logged in as Admin')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="nav-profile"]/a/img')

@then('the admin page is loaded')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="button-setting"]')


# scenario #2 - Change product details
@given('a product is already listed') 
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="menu-catalog"]/a').click()
    context.driver.find_element("xpath", '//*[@id="collapse-1"]/li[2]/a').click()
    time.sleep(2)
    context.driver.find_element("xpath", '//td[7]/div/a/i').click()

@given('user makes valid changes')
def step_impl(context):
    pass

@when('user clicks on "Save"')
def step_impl(context):
    context.driver.find_element("css selector", '#content > div.page-header > div > div > button > i').click()

@then('changes are applied')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element("xpath", '//*[@id="alert"]')


# scenario #3 - Remove customer account
@given('a user account exists') 
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="menu-customer"]/a').click()
    context.driver.find_element("xpath", '//*[@id="collapse-5"]/li[1]/a').click()
    time.sleep(2)
    context.driver.find_element("xpath", '//*[@id="form-customer"]/div[1]/table/tbody/tr[1]/td[3]')

@given('user has selected an account')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="form-customer"]/div[1]/table/tbody/tr[1]/td[1]/input').click()

@when('user clicks on "Delete"')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="content"]/div[1]/div/div/button[2]').click()
    time.sleep(1)
    context.driver.switch_to.alert.accept()

@then('the desired account is removed')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element("xpath", '//*[@id="alert"]')
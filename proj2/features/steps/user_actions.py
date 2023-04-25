from behave import *
import time


# scenario #1 Successful registration
@given('user has filled in valid information')
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8090/en-gb?route=account/register')
    text_area = context.driver.find_element("xpath", '//*[@id="input-firstname"]')
    text_area.send_keys('test1')
    text_area = context.driver.find_element("xpath", '//*[@id="input-lastname"]')
    text_area.send_keys('test2')
    text_area = context.driver.find_element("xpath", '//*[@id="input-email"]')
    text_area.send_keys('test1.test2@email.cz')
    text_area = context.driver.find_element("xpath", '//*[@id="input-password"]')
    text_area.send_keys('testpwd1')

@given('user\'s E-mail is not yet in use')
def step_impl(context):
    pass

@given('user has checked the Privacy Policy checkbox')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="form-register"]/div/div/div/input').click()   

@when('user clicks on "Continue"')
def step_impl(context):
    context.driver.find_element("css selector", '#form-register > div > div > button').click()

@then('user has been successfully registered')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element("css selector", '#common-success > ul > li:nth-child(3) > a')
    

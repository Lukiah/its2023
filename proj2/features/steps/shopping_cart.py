from behave import *
import time

# scenario #1 - Add to cart
@given('a product is listed')
def step_impl(context):
    context.driver.get(context.base_url)

@when('user clicks "Add to Cart" on a product')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element("css selector", '.col:nth-child(1) > form .img-fluid').click()
    time.sleep(0.5)
    context.driver.find_element("id", 'button-cart').click()

@then('the product is added to cart')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element("xpath", '//*[@id="alert"]')


# scenario #3 - Remove from cart
@given('single product is currently in the cart')
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8090/en-gb?route=checkout/cart')
    time.sleep(1)
    context.driver.find_element("xpath", '//*[@id="content"]/div[3]/div[2]/a')

@when('user clicks on "Remove"')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="shopping-cart"]/div/table/tbody/tr/td[4]/form/div/button[2]').click()
    time.sleep(1)

@then('Shopping Cart is empty')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="content"]/p')
        
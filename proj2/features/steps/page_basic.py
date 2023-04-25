from behave import *


# scenario #1 - Application loading
@given('user has network connection') 
def step_impl(context):
    pass

@given('user has a compatible browser')
def step_impl(context):
    pass

@when('user accesses the application link')
def step_impl(context):
    context.driver.get(context.base_url)

@then('web application loads correctly')
def step_impl(context):
    context.driver.find_element("xpath", "//button[@type='button']")


# scenario #2 - Changing the preffered currency
@given('"Currency" dropdown menu is visible')
def step_impl(context):
    context.driver.find_element("xpath", "//form[@id='form-currency']/div/a").click()
    context.driver.find_element("xpath", "//a[contains(text(),'€ Euro')]")

@when('user clicks the preffered currency')
def step_impl(context):
    context.driver.find_element("xpath", "//a[contains(text(),'€ Euro')]").click()

@then('the currency changes accordingly')
def step_impl(context):
    context.driver.find_element("xpath", "//strong[contains(.,'€')]")

@then('the currency stays changed on other pages')
def step_impl(context):
    context.driver.find_element("xpath", "//img[@alt='MacBook']").click()
    context.driver.find_element("xpath", "//strong[contains(.,'€')]")


# scenario #3 - Home page navigation
@given('user is on any catalog page')
def step_impl(context):
    context.driver.get(context.base_url)
    context.driver.find_element("xpath", "//img[@alt='MacBook']").click()

@when('user clicks the home page button')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@id='product-info']/ul/li/a/i").click()

@then('the home page is loaded')
def step_impl(context):
    context.driver.get(context.base_url)


# scenario #4 - Searching for products
@given('user enters product name into the search field') 
def step_impl(context):
    text_area = context.driver.find_element("xpath", "//input[@name='search']")
    text_area.send_keys("macbook")

@given('the product is listed')
def step_impl(context):
    pass

@when('user clicks the search button')
def step_impl(context):
    context.driver.find_element("xpath", '//div[@id="search"]/button/i').click()

@then('the desired product is shown')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="product-list"]/div[1]/form/div/div[2]/div[1]/h4/a')

# scenario #5 - Product detail page
@given('user is situated on any catalog page') 
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8090/en-gb/catalog/component/monitor')

@given('at least one product is listed')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="product-list"]/div[1]/form/div/div[1]/a/img')    

@when('user clicks on the product image')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="product-list"]/div[1]/form/div/div[1]/a/img').click()

@then('product page with details is displayed')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="content"]/div[1]/ul/li[1]/a')

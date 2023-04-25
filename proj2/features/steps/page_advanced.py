from behave import *
import time


# scenario #1 - Products comparison
@given('multiple products were added to comparison') 
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8090/en-gb/catalog/component/monitor')
    context.driver.find_element("xpath", '//*[@id="product-list"]/div[1]/form/div/div[2]/div[2]/button[3]').click()
    time.sleep(0.5)
    context.driver.find_element("xpath", '//*[@id="product-list"]/div[2]/form/div/div[2]/div[2]/button[3]').click()
    time.sleep(0.5)
    
@when('user clicks on "Product Compare"')
def step_impl(context):
    context.driver.find_element("id", 'compare-total').click()

@then('the added products are shown in comparison table')
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8090/en-gb?route=product/compare')
    context.driver.find_element("xpath", '//strong[contains(.,\'Apple Cinema 30"\')]')
    context.driver.find_element("xpath", '//strong[contains(.,\'Samsung SyncMaster 941BW\')]')
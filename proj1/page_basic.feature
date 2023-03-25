Feature: Basic application functionality

    Scenario: Application loading
        Given user has network connection
        And user has a compatible browser
        And user has a correct link
        When user accesses the application link
        Then web application fully loads

    Scenario: Changing the preffered currency
        Given the application page is loaded completely
        And user clicks on "Currency"
        When user clicks the preffered currency
        Then the currency changes correctly
        And the currency stays changed on other pages

    Scenario: Home page navigation
        Given user is on any page under the catalog section
        When user clicks the home page button
        Then the home page is loaded

    Scenario: Searching for products
        Given user enters the correct name of a product
        And the product is in-stock
        When user clicks the search button
        Then the desired product is shown



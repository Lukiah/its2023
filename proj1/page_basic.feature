Feature: Basic application functionality

    Scenario: Application loading
        Given user has network connection
        And user has a compatible browser
        When user accesses the application link
        Then web application loads correctly

    Scenario: Changing the preffered currency
        Given "Currency" dropdown menu is visible
        When user clicks the preffered currency
        Then the currency changes accordingly
        And the currency stays changed on other pages

    Scenario: Home page navigation
        Given user is on any catalog page
        When user clicks the home page button
        Then the home page is loaded

    Scenario: Searching for products
        Given user enters product name into the search field
        And the product is listed
        When user clicks the search button
        Then the desired product is shown

    Scenario: Product detail page
        Given user is situated on home page
        And at least one product is listed
        When user clicks on the product image
        Then product page with details is displayed


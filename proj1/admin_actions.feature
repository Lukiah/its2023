Feature: Administration access features

    Scenario: Admin login
        Given user enters valid login information
        When user clicks on "Login"
        Then user is successfully logged in as Admin
        And the admin page is loaded

    Scenario: View customer orders
        Given user is logged in as admin
        And one or more customer orders were placed
        When user accesses the Orders page
        Then placed orders are displayed

    Scenario: Add to calatog
        Given product is not yet listed 
        And user has filled in necessary information
        When user clicks on "Save"
        Then new product is added

    Scenario: Change product details
        Given a product is already listed
        And user makes valid changes
        When user clicks on "Save"
        Then changes are applied

    Scenario: Remove customer account
        Given a user account exists
        And user has selected an account
        When user clicks on "Delete"
        Then the desired account is removed

    Scenario: Change order status
        Given a pending order exists
        When user chooses order status "Processing"
        And user clicks on "Add History"
        Then the order status is changed to "Processing"
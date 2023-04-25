Feature: Administration access features

    Scenario: Admin login
        Given user enters valid login information
        When user clicks on "Login"
        Then user is successfully logged in as Admin
        And the admin page is loaded

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

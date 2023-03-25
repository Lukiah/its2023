Feature: User account interactions

    Scenario: Successful registration
        Given the current loaded page is registration
        And user fills in valid information
        And user's E-mail is not yet in use
        And user checks the Privacy Policy checkbox
        When "Continue" button is clicked
        Then a page informing about successful registration loads


    Scenario: Unsuccessful registration
        Given the current loaded page is registration
        And user fills in valid information
        And user's E-mail is already in use
        And user checks the Privacy Policy checkbox
        When "Continue" button is clicked
        Then a warning displays that E-mail is in use

    Scenario: Successful password change
        Given 

    Scenario: Unsuccessful password change
        Given 
        
    Scenario: Successful login to wishlist page
        Given the user has created an account
        And user is currently logged out
        And clicked the "Wish List" button
        And correct login information is inserted
        When user clicks the "Login" button
        Then user is logged in 
        And user's wishlist is loaded

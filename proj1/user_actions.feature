Feature: User account interactions

    Scenario: Successful registration
        Given user has filled in valid information
        And user's E-mail is not yet in use
        And user has checked the Privacy Policy checkbox
        When user clicks on "Continue"
        Then user has been successfully registered

    Scenario: Unsuccessful registration
        Given user has filled in valid information
        And user's E-mail is already in use
        And user checks the Privacy Policy checkbox
        When user clicks on "Continue"
        Then a warning informs that E-mail is in use
    
    Scenario: Successful login
        Given user is currently logged out
        And correct login information is inserted
        When user clicks the "Login" button
        Then user is logged in

    Scenario: Successful password change
        Given user is logged in
        When user inputs matching passwords
        And user clicks "Continue"
        Then password is successfully updated

    Scenario: Unsuccessful password change
        Given user is logged in
        When user inputs non-matching passwords
        And user clicks "Continue"
        Then the password remains unchanged
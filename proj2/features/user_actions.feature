Feature: User account interactions

    Scenario: Successful registration
        Given user has filled in valid information
        And user's E-mail is not yet in use
        And user has checked the Privacy Policy checkbox
        When user clicks on "Continue"
        Then user has been successfully registered
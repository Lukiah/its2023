Feature: Advanced application functionality

    Scenario: Products comparison
        Given multiple products were added to comparison
        When user clicks on "Product Compare"
        Then the added products are shown in comparison table

    Scenario: Add to Wish List
        Given user is logged in
        And one or more products were added to Wish List
        When users clicks on "Wish List"
        Then the added products are displayed

    Scenario: Newsletter subscription
        Given user is not yet subscribed
        When user checks "Yes"
        And user clicks "Continue"
        Then a message confirms successful subscription

    Scenario: Contact us
        Given user is logged in
        And user fills in the Contact form
        When user clicks "Submit"
        Then an enquiry is sent
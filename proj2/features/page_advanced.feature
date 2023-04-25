Feature: Advanced application functionality

    Scenario: Products comparison
        Given multiple products were added to comparison
        When user clicks on "Product Compare"
        Then the added products are shown in comparison table

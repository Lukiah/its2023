Feature: Shopping cart interactions

    Scenario: Add to cart
        Given a product is listed
        When user clicks "Add to Cart" on a product
        Then the product is added to cart

    Scenario: View cart content
        Given a product has been added to cart
        When user clicks on "View Cart"
        Then Shopping Cart content is displayed

    Scenario: Remove from cart
        Given single product is currently in the cart
        When user clicks on "Remove"
        Then Shopping Cart is empty
        And there is no option to checkout

    Scenario: Checkout page
        Given products are currently in the cart
        When user clicks on "Checkout"
        Then the checkout page is loaded
        And final price is displayed

    Scenario: Successful checkout
        Given user has filled in valid information
        And user chose shipping and payment method
        When user clicks on "Confirm Order"
        Then an order has been placed successfully
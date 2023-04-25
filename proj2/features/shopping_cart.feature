Feature: Shopping cart interactions

    Scenario: Add to cart
        Given a product is listed
        When user clicks "Add to Cart" on a product
        Then the product is added to cart

    Scenario: Remove from cart
        Given single product is currently in the cart
        When user clicks on "Remove"
        Then Shopping Cart is empty

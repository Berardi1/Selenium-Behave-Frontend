Feature: Product Store
  In order to buy a product
  As a customer
  I want to browse the store



 Background:
        Given I navigate to Demoblaze
        And Im logged in


  Scenario: open a product
        When I open a product
        Then I should see the product details


   Scenario: add a product to cart
        When I open a product
        And I added the product to the cart
        Then I should see the "Product added." alert message
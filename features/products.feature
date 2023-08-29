Feature: Product Store
  In order to buy a product
  As a customer
  I want to browse the store



 Background:
        Given I navigate to Demoblaze
        #And I am logged in

  @smoke
  Scenario: open a product
        When I open a product
        Then I should see the product details

  @sanity
   Scenario: add a product to cart
        When I open a product
        And I added the product to the cart
        Then I should get a "Product added" alert
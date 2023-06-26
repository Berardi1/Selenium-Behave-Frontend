Feature: Cart
  In order to complete my purchase
  As a customer
  I want to view the cart


    Background:
        Given I navigate to Demoblaze
        And I am logged in


  Scenario: review products
        Given add a product to the cart
        When I open the cart
        Then I should see the product


  Scenario: purchase order
        Given I add a product to the cart
        When open the cart
        And purchase the order
        Then I should see that the purchase is confirmed


  Scenario: remove a product
        Given I add a product to the cart
        When I open the cart
        And I remove the first product
        Then I should see that a product was removed
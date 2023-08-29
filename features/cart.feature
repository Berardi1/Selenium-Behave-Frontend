@cart
Feature: Cart
  In order to complete my purchase
  As a customer
  I want to view the cart


    Background:
        Given I navigate to Demoblaze
        #And I am logged in

  @smoke
  Scenario: review products
        Given I add a product to the cart
        When I open the cart
        Then I should see the product

  @sanity
  Scenario: purchase order
        Given I add a product to the cart
        When I open the cart
        And I place the order
        And purchase the order
        Then I should see that the purchase is confirmed

  @sanity
  Scenario: remove a product
        Given I add a product to the cart
        When I open the cart
        And I remove the first product
        Then I should see that a product was removed
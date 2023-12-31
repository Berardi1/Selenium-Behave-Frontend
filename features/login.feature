@login
Feature: Login
  In order to manage my account
  as a customer
  I want to login

   Background:
        Given I navigate to Demoblaze

  @smoke
   Scenario:  login with valid parameters
     When I open the login modal
     And I enter valid email and password into the fields
     Then I should be correctly logged in
  @regression
   Scenario: Login with invalid email and valid password
     When I open the login modal
     And I enter invalid email and valid password into the fields
     Then I should get a "User does not exist." alert
  @regression
   Scenario: Login with valid email and invalid password
     When I open the login modal
     And I enter valid email and invalid password into the fields
     Then I should get a "Wrong password." alert
  @regression
   Scenario: Login with invalid credentials
     When I open the login modal
     And I enter invalid email and invalid password into the fields
     Then I should get a "Wrong password." alert
  @regression
   Scenario: Login without entering any credentials
     When I open the login modal
     And I dont enter anything into email and password fields
     Then I should get a "Please fill out Username and Password." alert
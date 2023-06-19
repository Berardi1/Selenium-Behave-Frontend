Feature: Signup Account functionality


  Background:
        Given I navigate to Demoblaze

  Scenario:  Signup with valid parameters
    When I open the signup field
    And I enter all my fields
    Then Account should get created

  Scenario:  Signup with empty username
    When I open the signup field
    And I enter only a password
    Then I should get a "Please fill out Username and Password." alert

  Scenario:  Signup with empty password
    When I open the signup field
    And I enter only a username
    Then I should get a "Please fill out Username and Password." alert

  Scenario: Signup with empty field
    When I open the signup field
    And I dont enter anything into the fields
    Then I should get a "Please fill out Username and Password." alert
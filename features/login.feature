Feature: User Login
  As a user
  I want to login to the application
  So that I can access my account

  Background:
    Given I am on the login page

  Scenario: Successful login with valid credentials
    When I enter username "admin" and password "password123"
    #And I click the login button
    #Then I should be redirected to the dashboard
    #And I should see a welcome message

  Scenario: Failed login with invalid credentials
    When I enter username "invalid" and password "wrong"
    And I click the login button
    Then I should see an error message "Invalid credentials"
    And I should remain on the login page

  Scenario Outline: Login with different user types
    When I enter username "<username>" and password "<password>"
    And I click the login button
    Then I should see "<expected_result>"

    Examples:
      | username | password    | expected_result |
      | admin    | password123 | Welcome Admin   |
      | user     | userpass    | Welcome User    |
      | guest    | guestpass   | Welcome Guest   |
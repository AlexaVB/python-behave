Feature: Sample

  Scenario: Login error message
    Given a browser
    When I visit "https://google.com"
    Then I should see the google page has loaded

  Scenario: Signing in
    Given I use my email address to attempt to sign into google
    Then I should see that I should try a different browser to sign in

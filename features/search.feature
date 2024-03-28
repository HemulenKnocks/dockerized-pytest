Feature: Search

  Scenario: Search for information on the home page
    Given The Home Page is loaded
    When Enter the input in search field
    Then Related information will be displayed

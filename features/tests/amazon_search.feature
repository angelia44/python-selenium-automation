# Created by leeya at 5/17/2023
Feature: Amazon Search tests
  # Enter feature description here

  Scenario: User can search on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results shown for "table"

  Scenario: User can search on Amazon
    Given Open amazon main page
    When Search for coffee
    Then Verify search results shown for "coffee"
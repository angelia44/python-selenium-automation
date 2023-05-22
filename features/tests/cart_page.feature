# Created by leeya at 5/19/2023
Feature: Cart Page test

  Scenario: Verify Cart is empty
    Given Open amazon main page
    When Click on Cart
    Then Verify cart is empty
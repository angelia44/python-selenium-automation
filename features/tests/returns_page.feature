# Created by leeya at 5/18/2023
Feature: Returns Page Test
  Scenario: User sees sign in
    Given Open amazon main page
    When Click on Returns and Orders
    Then Verify Sign in title exists
    Then Verify email input is present
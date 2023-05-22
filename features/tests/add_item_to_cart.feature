# Created by leeya at 5/19/2023
Feature: Add Item to Cart
  Scenario: User can add item to cart
    Given Open amazon main page
    When Search for 3d Printers
    When Click third result
    When Add item to Cart
    When Navigate to Cart Page
    Then Verify item is in cart

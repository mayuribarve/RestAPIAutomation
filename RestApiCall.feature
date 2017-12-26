# Created by mayurib at 11/27/2017
Feature: WeatherMap REST API call testing
  # Enter feature description here


  Scenario: Send GET Request
    Given Set GET api endpoint
    #When Set HEADER param request content type as "application/json"
    #And Set HEADER param response accept type as "application/json"
    When Raise "GET" HTTP request
    Then Valid HTTP response should be received
    And Assert that response status code is 200
    And Assert that name key in response contains 'Mountain View' value
    And Assert that weather object has id, main, description and icon fields

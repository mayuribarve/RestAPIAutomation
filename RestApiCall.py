from behave import given, when, then, step
import requests
import json
import nose
from nose.tools import assert_equal

url = "http://samples.openweathermap.org/data/2.5/weather?zip=07110,us&appid=b1b15e88fa797225412429c1c50c122a1"
response = ""
responsedata = ""


@given("Set base URL")
def step_impl(context):
    url = "http://samples.openweathermap.org"
    pass


# Scenario Send GET Request
@given("Set GET api endpoint")
def stel_impl(context):
    try:
        assert True
        assert url != ""
        print("Set GET API endpoint")
    except AssertionError:
        print("Invalid API endpoint")
        exit(1)


@when('Raise "GET" HTTP request')
def step_impl(context):
    try:
        assert True
        response = requests.get(url)
        assert response != ""
        responsedata = response.json()
    except AssertionError:
        print("GET API request returns invalid response")
        pass


# Assert Response Status Code
@then("Valid HTTP response should be received")
@step("Assert that response status code is 200")
def step_impl(context):
    try:
        assert True
        assert response.status_code == "200"
        print("Response format is valid")
    except AssertionError:
        print("Invalid response status code")
        exit(1)


# Assert that name key in response contains 'Mountain View' value
@step("Assert that name key in response contains 'Mountain View' value")
def step_impl(context):
    try:
        assert True
        assert responsedata['name'] == "Mountain View"
        print("name key in response contains 'Mountain View' value")
    except AssertionError:
        print("name key does not have 'Mountain View' value")
        pass


# Assert that weather object contains id, main, description and icon values
@step("Assert that weather object has id, main, description and icon fields")
def step_impl(context):
    try:
        assert True
        weatherinfo = responsedata['weather']
        assert weatherinfo[0]['id'] != ""
        print("\n weather object has 'id' field set")
        assert weatherinfo[0]['main'] != ""
        print("\n weather object has 'main' field set")
        assert weatherinfo[0]['description'] != ""
        print("\n weather object has 'description' field set")
        assert weatherinfo[0]['icon'] != ""
        print("\n weather object has 'icon' field set")
    except AssertionError:
        print("weather object has some invalid field data")
        pass

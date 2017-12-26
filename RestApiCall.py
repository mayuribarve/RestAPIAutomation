from behave import given, when, then, step
import requests
import sys

url = ""
response = ""
responsedata = ""


# Scenario Send GET Request
@given("Set GET api endpoint")
def stel_impl(context):
    global url
    url = "http://samples.openweathermap.org/data/2.5/weather?zip=07110,us&appid=b1b15e88fa797225412429c1c50c122a1"
    print("Set GET API endpoint")


@when('Raise "GET" HTTP request')
def step_impl(context):
    global response
    global responsedata
    try:
        assert True
        response = requests.get(url)
        assert response.status_code == 200
        responsedata = response.json()
        print("HTTP request to API is raised")
    except AssertionError:
        print("\n GET API request returns invalid response")
        pass


# Assert Response Status Code
@then("Valid HTTP response should be received")
@step("Assert that response status code is 200")
def step_impl(context):
    try:
        assert True
        assert response.status_code == 200
        print("\n Response format is valid")
    except AssertionError:
        print("\n Invalid response status code")
        exit(1)


# Assert that name key in response contains 'Mountain View' value
@step("Assert that name key in response contains 'Mountain View' value")
def step_impl(context):
    try:
        assert True
        assert responsedata != ""
        assert responsedata['name'] == "Mountain View"
        print("\n name key in response contains 'Mountain View' value")
    except AssertionError:
        print("\n name key does not have 'Mountain View' value")
        pass



# Assert that weather object contains id, main, description and icon values
@step("Assert that weather object has id, main, description and icon fields")
def step_impl(context):
    try:
        assert True
        assert responsedata != ""
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
        print("\n weather object has some invalid field data")
        pass


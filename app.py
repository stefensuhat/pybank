from flask import Flask, jsonify, request
from waitress import serve

from automate import TestAppium

app = Flask(__name__)


@app.route("/")
def hello_world():
    appiumClass = TestAppium()

    appiumClass.setup()
    run = appiumClass.test_find_about_phone()
    # Get the action from the request body
    # action = request.get_json()['action']

    # # Initialize Appium
    # desired_capabilities = {'platformName': 'Android', 'deviceName': 'emulator-5554'}
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    # # Perform the action using Appium
    # if action == 'click_button':
    #     driver.find_element_by_accessibility_id('my_button').click()
    # elif action == 'enter_text':
    #     driver.find_element_by_id('my_text_field').send_keys('Hello, World!')

    # Return the result
    return jsonify({"result": run})


if __name__ == "__main__":
    serve(app.run(debug=True), threads=2)

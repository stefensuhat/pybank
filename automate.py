import subprocess
import time
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions

capabilities = dict(
    platformName="Android",
    automationName="uiautomator2",
    deviceName="Android",
    appPackage="com.android.settings",
    appActivity=".Settings",
    language="en",
    locale="US",
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


appium_server_url = "http://localhost:4723"


class TestAppium(unittest.TestCase):
    def __init__(self) -> None:
        self.appium_process = None
        self.driver = None

    def start_appium_server(self) -> None:
        self.appium_process = subprocess.Popen(
            ["appium"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        time.sleep(5)

    def setup(self) -> None:
        self.start_appium_server()

        appium_options = AppiumOptions()
        appium_options.load_capabilities(capabilities)
        driver = webdriver.Remote(appium_server_url, options=appium_options)
        # self.driver = webdriver.Remote(appium_server_url, capabilities)

        self.driver = driver

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_about_phone(self) -> None:
        driver = self.driver
        # el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Connections"]')
        # el = self.driver.find_element(by=AppiumBy.XPATH, value='android:id/title')
        # Scroll until the element is visible
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector()).scrollIntoView(text("Security and privacy"))',
        )

        # Wait until the element is visible
        el = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Security and privacy"]',
                )
            )
        )
        el.click()


if __name__ == "__main__":
    unittest.main()

import subprocess
import time
import unittest
import os
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService

appium_service = AppiumService()

capabilities = dict(
    platformName="Android",
    automationName="uiautomator2",
    deviceName="Android",
    appPackage="com.android.settings",
    appActivity=".Settings",
    language="en",
    locale="US",
)

appium_server_url = "http://localhost:4723"


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        # self.start_appium_server()
        # if os.name == "nt":
        #     os.system("start /B start cmd.exe @cmd /k appium")
        # else:
        #     os.system("start /B start cmd.exe @cmd /k appium")
        appium_service.start()

        appium_options = AppiumOptions()
        appium_options.load_capabilities(capabilities)
        self.driver = webdriver.Remote(appium_server_url, options=appium_options)

    # def start_appium_server(self) -> None:
    #     self.appium_process = subprocess.Popen(
    #         ["cmd", "/c", "appium"],
    #         stdout=subprocess.PIPE,
    #         stderr=subprocess.PIPE,
    #         shell=True,
    #     )
    #     time.sleep(5)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
        if appium_service.is_running():
            appium_service.stop()

    def test_find_security_and_privacy(self) -> None:
        # Scroll until the element is visible
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector()).scrollIntoView(text("Security and privacy"))',
        )

        # Wait until the element is visible
        el = WebDriverWait(self.driver, 10).until(
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

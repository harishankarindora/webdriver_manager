from webdriver_manager import config
from webdriver_manager.driver import FireFoxDriver
from webdriver_manager.manager import DriverManager
from webdriver_manager import utils


class GeckoDriverManager(DriverManager):
    def __init__(self, version="latest",
                 name="geckodriver",
                 url="https://github.com/mozilla/geckodriver/releases/download",
                 os_type=utils.os_name()):
        DriverManager.__init__(self)
        self.driver = FireFoxDriver(driver_url=url,
                                    name=name,
                                    version=version,
                                    os_type=os_type)

    def install(self):
        return self._file_manager.download_driver(self.driver).path

    def use_token(self, token):
        config.gh_token = token
        return self

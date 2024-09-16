import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class DarkModeTest(unittest.TestCase):

    def setUp(self):
        # Provide the path to your Chrome WebDriver executable
        
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://swarna.bchrd.org/wp-admin/"

        ENV_FILE = ".env"
        if os.path.exists(ENV_FILE):
            with open(ENV_FILE, "r") as f:
                for line in f.readlines():
                    key, value = line.strip().split("=")
                    os.environ[key] = value
        else:
            print(f"Error: {ENV_FILE} not found. Please create it following instructions in .env.example")
            exit(1)

        WORDPRESS_URL = os.getenv("WORDPRESS_URL")+'/wp-admin/'
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.base_url = WORDPRESS_URL
    def test_dark_mode(self):
        self.login(self.username, self.password)
        if not self.is_plugin_active("WP Dark Mode"):
            self.install_and_activate_plugin("WP Dark Mode")
        self.enable_backend_darkmode()
        self.assert_backend_darkmode_enabled()
        self.navigate_to_wp_dark_mode_settings()
        # self.change_floating_switch_style()
        # self.set_custom_switch_size(220)
        # self.change_floating_switch_position("left_bottom")
        # self.disable_keyboard_shortcut()
        # self.enable_darkmode_toggle_animation()
        # self.assert_frontend_darkmode_enabled()

    def tearDown(self):
        self.driver.quit()

    # Helper methods
    def login(self, username, password):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "user_login").send_keys(username)
        self.driver.find_element(By.ID, "user_pass").send_keys(password)
        self.driver.find_element(By.ID, "wp-submit").click()

    # def is_plugin_active(self, plugin_name):
    #     self.driver.get(self.base_url + "plugins.php")
    #     try:
    #         return self.driver.find_element(By.XPATH, f"//tr[contains(., '{plugin_name}')]/td[@class='plugin-title column-primary']/strong[text()='Active']") is not None
    #     except:
    #         return False
    def is_plugin_active(self, plugin_name):
        print(f"Checking if '{plugin_name}' plugin is active...")

        # Navigate to the Plugins page
        self.driver.get(self.base_url + "plugins.php")

        # Wait for the Plugins page to load
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID, "the-list")))

        # Find all plugin rows
        plugin_rows = self.driver.find_elements(By.XPATH, "//tr[contains(@class, 'active') or contains(@class, 'inactive')]")
        
        # Check if the plugin is installed
        
        for plugin_row in plugin_rows:
            plugin_title = plugin_row.find_element(By.CLASS_NAME, "plugin-title").text
            print(plugin_title)
            if plugin_name in plugin_title:
                # Check if the plugin is active
                is_active = plugin_row.find_elements(By.XPATH, ".//a[contains(@class, 'deactivate')]")
                if is_active:
                    print(f"'{plugin_name}' plugin is active.")
                    return True
                else:
                    print(f"'{plugin_name}' plugin is installed but not active. Activating...")
                     # Activate the plugin
                    # activate_link = plugin_row.find_element(By.XPATH, ".//a[contains(@class, 'activate-now')]")
                    activate_link = plugin_row.find_element(By.LINK_TEXT, "Activate")
                    activate_link.click()
                    print(f"'{plugin_name}' plugin has been activated.")
                    return True
        
        print(f"'{plugin_name}' plugin is not installed.")
        return False


    def install_and_activate_plugin(self, plugin_name):
        print("Navigating to plugin installation page...")
        self.driver.get(self.base_url + "plugin-install.php?s=" + plugin_name + "&tab=search&type=term")

        # Wait for the "Install Now" button to be present on the page
        print("Waiting for 'Install Now' button...")
        install_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Install Now"))
        )
        print("'Install Now' button found.")
        # Scroll into view if necessary
        self.driver.execute_script("arguments[0].scrollIntoView();", install_button)
        print("Scrolling to 'Install Now' button.")
        install_button.click()

        # Wait for the "Activate" button to be clickable after installation
        print("Waiting for 'Activate' button after installation...")
        activate_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Activate"))
        )
        print("'Activate' button found.")
        activate_button.click()
        print("Plugin installation and activation completed successfully.")




    def enable_backend_darkmode(self):
            self.driver.get(self.base_url + "options-general.php?page=wp-dark-mode")
            # self.driver.find_element(By.ID, "wp_dark_mode_admin_bar_switcher_enable").click()
            element=self.driver.find_element(By.XPATH, '//*[@id="wp-dark-mode-admin"]/div/div/div/div[2]/div[3]/section[1]/div[1]/div[1]/label/div[1]/div')
            element.click()
            print("Switched to ON/OFF")
            # self.driver.find_element(By.NAME, "submit").click()

    def assert_backend_darkmode_enabled(self):
        self.driver.get(self.base_url + "wp-admin/")
        assert self.driver.find_element(By.ID, "wp-dark-mode-bar") is not None

    def navigate_to_wp_dark_mode_settings(self):
        self.driver.get(self.base_url + "options-general.php?page=wp_dark_mode")

    def change_floating_switch_style(self):
        style_dropdown = self.driver.find_element(By.ID, "wp_dark_mode_admin_bar_switcher_style")
        style_dropdown.click()
        style_dropdown.find_element(By.XPATH, "//option[text()='Square']").click()
        self.driver.find_element(By.NAME, "submit").click()

    def set_custom_switch_size(self, size):
        size_input = self.driver.find_element(By.ID, "wp_dark_mode_admin_bar_switcher_size")
        size_input.clear()
        size_input.send_keys(size)
        self.driver.find_element(By.NAME, "submit").click()

    def change_floating_switch_position(self, position):
        position_dropdown = self.driver.find_element(By.ID, "wp_dark_mode_admin_bar_switcher_position")
        position_dropdown.click()
        position_dropdown.find_element(By.XPATH, f"//option[text()='{position.capitalize()}']").click()
        self.driver.find_element(By.NAME, "submit").click()

    def disable_keyboard_shortcut(self):
        self.driver.find_element(By.ID, "wp_dark_mode_disable_shortcut").click()
        self.driver.find_element(By.NAME, "submit").click()

    def enable_darkmode_toggle_animation(self):
        self.driver.find_element(By.ID, "wp_dark_mode_darkmode_toggle_animation").click()
        self.driver.find_element(By.ID, "wp_dark_mode_darkmode_toggle_animation_type").send_keys("fade")
        self.driver.find_element(By.NAME, "submit").click()

    def assert_frontend_darkmode_enabled(self):
        # Implementation for asserting frontend dark mode enabled
        pass

if __name__ == "__main__":
    unittest.main()

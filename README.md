# Dark Mode Test Suite

This test suite is designed to test the functionality of the Dark Mode feature on a WordPress admin panel. It utilizes Selenium for browser automation and unittest for test organization.

## Requirements

1. **Python**: Ensure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).
   
2. **Selenium**: Install Selenium using pip:

    ```
    pip install selenium
    ```

3. **Chrome WebDriver**: Download the Chrome WebDriver executable compatible with your Chrome browser version and place it in your system's PATH. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Environment Variables

This test suite requires certain environment variables to be set. Please create a `.env` file following the structure in `.env.example` provided in the repository. Populate the following variables:

- `WORDPRESS_URL`: URL of your WordPress admin panel.
- `USERNAME`: Username for logging into WordPress.
- `PASSWORD`: Password for logging into WordPress.

## Running the Test Suite

1. Clone this repository to your local machine:

    ```
    git clone <repository_url>
    ```

2. Navigate to the cloned directory:

    ```
    cd AutomationWithWP
    ```

3. Set up the environment variables by creating a `.env` file and populating it as mentioned above.

4. Run the test suite using the following command:

    ```
    python dark_mode_test.py
    ```



## Scenarios

1. Log in to your WordPress site.
2. Check whether the "WP Dark Mode" Plugin is Active or not.
3. If Active, navigate to the WP Dark Mode & continue. Otherwise, Install the Plugin and Activate it.
4. Enable Backend Darkmode from Settings Settings -> General.
5. Validate whether the Darkmode is working or not on the Admin Dashboard.
6. Navigate to the WP Dark Mode.
7. From Settings -> Switch Settings Change the "Floating Switch Style" from the default selections (Select any one from the available options, except the default selected one).
8. From Settings -> Switch Select Custom Switch size & Scale it to 220.
9. From Settings -> Switch Settings Change the Floating Switch Position (Left Bottom).
10. Disable Keyboard Shortcut from the Accessibility Settings.
11. From Settings -> Animation Enable "Darkmode Toggle Animation" & change the "Animation Effect" from the default selections (Select any one from the available options, except the default selected one).
12. Validate whether the Darkmode is working or not from the Frontend.

* Save the settings every time after changing it.
* Do not share your credentials on the GitHub repo. Use a .env file to store the credentials and please add a .env.example (Containing the instructions to create the env file) file to the GitHub repo.



## Test Cases

The `DarkModeTest` class contains test cases for verifying the functionality of the Dark Mode feature on the WordPress admin panel. You can extend these test cases or add new ones as per your requirements.

## Note

- Ensure that you have a stable internet connection while running the test suite, as it interacts with the WordPress admin panel.
- Make sure your WordPress site is accessible during the test execution.



## GitAction Integration (Bonus)

You can integrate the test suite with GitAction to automatically run tests on every push. Here's how to set it up:

1. Create a workflow file (e.g., `tests.yml`) in the `.github/workflows` directory in your repository.

2. Configure the workflow file to execute the test suite. Here's a basic example:

    ```yaml
    name: Run Tests

    on:
      push:
        branches:
          - main

    jobs:
      test:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout Repository
            uses: actions/checkout@v2

          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.x'

          - name: Install dependencies
            run: |
              pip install selenium

          - name: Run Tests
            run: python <filename>.py
    ```

Replace `<filename>` with the name of the Python file containing the test suite (e.g., `dark_mode_test.py`).

3. Commit and push the changes to your repository. GitAction will automatically run the test suite on every push to the main branch.

That's it! Now your test suite will be automatically executed whenever changes are pushed to your repository.
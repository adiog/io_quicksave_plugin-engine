from selenium import webdriver


def save_screenshot(url, screenshot_file):
    browser = webdriver.Firefox()
    browser.get(url)
    browser.save_screenshot(screenshot_file)
    browser.quit()
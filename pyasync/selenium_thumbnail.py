from selenium import webdriver


def save_thumbnail(url, thumbnail_file):
    browser = webdriver.Firefox()
    browser.get(url)
    browser.save_screenshot(thumbnail_file)
    browser.quit()

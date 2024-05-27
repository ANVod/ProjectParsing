from selenium import webdriver

options = webdriver.ChromeOptions()

binary_yandex_driver_file = 'C:\Users\avody\Downloads\chromedriver.exe'  # путь к ChromeDriver
driver = webdriver.Chrome(executable_path=binary_yandex_driver_file, options=options)
driver.get('https://yandex.com')
driver.quit()
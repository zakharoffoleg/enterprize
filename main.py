from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

auth = {'zakharoffffff': 'VesennyDen99'}

url = 'https://wordstat.yandex.ru'
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(chrome_options=options)
driver.get(url)


def login():
    try:
        voiti_link = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Войти'))
        )
        voiti_link.click()
        print('Нажимаю "Войти"...')

        print(driver.find_elements_by_css_selector("input[name='login']"))

        try:
            login_selector = "#b-domik_popup-username"

            wait_login = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, login_selector))
            )
            login_form = driver.find_element_by_css_selector(login_selector)
            login_form.send_keys(next(iter(auth)))
            print("Ввожу логин...")

            try:
                pass_selector = "#b-domik_popup-password"

                wait_password = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, pass_selector))
                )
                pass_form = driver.find_element_by_css_selector(pass_selector)
                pass_form.send_keys(auth.get(next(iter(auth))))
                print("Ввожу пароль...")

                try:
                    voiti_btn = WebDriverWait(driver, 1).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    "div.b-domik__button span:first-child"))
                    )
                    voiti_btn.click()
                    print('Нажимаю кнопку...')

                finally:
                    driver.quit()
            finally:
                driver.quit()
        finally:
            driver.quit()
    finally:
        driver.quit()


login()

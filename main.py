from bs4 import BeautifulSoup
import mechanize
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://wordstat.yandex.ru'

auth = ('zakharoffffff', 'VesennyDen99')

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

xpath_login = "/html[@class='i-ua_js_yes i-ua_css_standart i-ua_svg_yes i-ua_inlinesvg_yes']/body[@class='b-page " \
              "b-page__body i-global i-bem i-global_js_inited b-page_js_inited']/form[@class='b-domik b-domik_type_" \
              "popup b-domik_position_top i-bem']/table[@class='b-domik__shadow']/tbody/tr[2]/td[@class='b-domik__" \
              "shadow__m']/div[@class='b-domik__form']/div[@class='b-domik__username']/span[@class='b-form-input b-" \
              "form-input_theme_grey b-form-input_size_m b-domik__input i-bem b-form-input_js_inited b-form-input_" \
              "focused_yes']/span[@class='b-form-input__box']/input[@id='b-domik_popup-username']"

xpath_pass = "/html[@class='i-ua_js_yes i-ua_css_standart i-ua_svg_yes i-ua_inlinesvg_yes']/body[@class='b-page b-" \
             "page__body i-global i-bem i-global_js_inited b-page_js_inited']/form[@class='b-domik b-domik_type_popup" \
             " b-domik_position_top i-bem']/table[@class='b-domik__shadow']/tbody/tr[2]/td[@class='b-domik__shadow__" \
             "m']/div[@class='b-domik__form']/div[@class='b-domik__password']/span[@class='b-form-input b-form-input" \
             "_theme_grey b-form-input_size_m b-form-input_type_password b-domik__input i-bem b-form-input_js_inited'" \
             "]/span[@class='b-form-input__box']/input[@id='b-domik_popup-password']"

xpath_login_btn = "/html[@class='i-ua_js_yes i-ua_css_standart i-ua_svg_yes i-ua_inlinesvg_yes']/body[@class='b-page" \
                  " b-page__body i-global i-bem i-global_js_inited b-page_js_inited']/form[@class='b-domik b-domik_" \
                  "type_popup b-domik_position_top i-bem']/table[@class='b-domik__shadow']/tbody/tr[2]/td[@class='b-" \
                  "domik__shadow__m']/div[@class='b-domik__form']/div[@class='b-domik__button']/span[@class='b-form-" \
                  "button b-form-button_size_m b-form-button_theme_grey-m b-form-button_valign_middle i-bem b-form-" \
                  "button_js_inited b-form-button_hovered_yes']/input[@class='b-form-button__input']"

try:
    element_voiti = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Войти'))
    )
    print(element_voiti.text)
    element_voiti.click()

    try:
        wait_login = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, xpath_login))
        )
        login_form = driver.find_element_by_xpath(xpath_login)
        login_form.send_keys("zakharoffffff")

        try:
            wait_password = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, xpath_pass))
            )
            pass_form = driver.find_element_by_xpath(xpath_pass)
            pass_form.send_keys("VesennyDen99")
            try:
                login_btn = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_login_btn))
                )
                login_btn.submit()
            finally:
                driver.quit()
        finally:
            driver.quit()
    finally:
        driver.quit()
finally:
    driver.quit()

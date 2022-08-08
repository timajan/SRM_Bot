from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as Bs

from config import *
import pickle
import time

# Налаштування браузера
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Браузер
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://app.hubspot.com/contacts/8082519/objects/0-1/views/my/list?redirectFrom=crm-records-ui')
driver.get('https://app.hubspot.com/contacts/8082519/objects/0-1/views/my/list?redirectFrom=crm-records-ui')


def get_data():
    """Функція для отримання сторінки зі посиланнями"""

    # использование куки для входа на сайт
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get('https://app.hubspot.com/contacts/8082519/objects/0-1/views/my/list?redirectFrom=crm-records-ui')
    driver.maximize_window()
    time.sleep(5)
    status = driver.find_element(By.XPATH,
        '/html/body/div[3]/div[1]/div/div/div/div/section/section/div/div[1]/div/div[1]/div[1]/div[4]/label/div')
    time.sleep(1 / 2)
    status.click()
    unassigned = driver.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/div/div[2]/div/label')
    unassigned.click()
    time.sleep(4)
    with open(f"index.html", "w", encoding='utf-8') as file:
        file.write(driver.page_source)


def get_url():
    """Функія для сбору посилань з сторінки"""
    urls_list = []
    get_data()
    with open('index.html', 'r', encoding='utf-8') as file:
        src = file.read()
    soup = Bs(src, 'lxml')

    urls = soup.find_all('a', class_='private-link uiLinkWithoutUnderline uiLinkDark')

    for url in urls:
        item = url.get('href')
        if 'contacts' in item:
            urls_list.append(f'{domain}{item}{email_field}')
    return urls_list


def send_emails():
    """Функція для відправки повідомлень"""
    count = 1
    for url in get_url():
        print(f"Сторінка номер {str(count)}")
        count += 1

        driver.get(url)
        driver.maximize_window()
        time.sleep(5)

        sub_field = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/div[2]/input')
        sub_field.send_keys(subject)
        time.sleep(1)

        main_field = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/div/div/div')
        main_field.send_keys(Keys.CONTROL, 'a')
        main_field.send_keys(Keys.DELETE)
        name = driver.title.split(' ')[0]
        main_field.send_keys(create_text(name))
        time.sleep(2)

        button_send = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div[3]/div/div[3]/div/div/div[1]/div/span/div/button[1]')
        button_send.click()
        time.sleep(2)

        status = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/aside/div[2]/ul/li[1]/div/section/div/div/div[2]/div/div/div/form/div[6]/div[1]')
        status.click()
        time.sleep(2)

        attempt = driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div/div/span/div/div[2]/div/div[3]/span/span/button')
        attempt.click()
        time.sleep(2)

        button_save = driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div/div[1]/button[1]')
        button_save.click()
        time.sleep(2)

    print("Робота завершена")


def main():
    try:
        send_emails()
    except Exception as ex:
        print(ex)
    finally:
        print('Робота зупинена')


if __name__ == "__main__":
    main()

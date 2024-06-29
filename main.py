import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
def login_user():

    driver.get("https://hh.ru/account/login?backurl=%2F&hhtmFrom=main&customDomain=1")
    login_element = driver.find_element(By.NAME, "login")
    login_element.clear()
    login_element.send_keys("@gmail.com")
    login_element.send_keys(Keys.RETURN)
    time.sleep(30)


def found_all_links(link_search: str):

    driver.get(link_search)

    try:
        wait = WebDriverWait(driver, 1)

        all_links = []

        controls_containers = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "controls-container--W4GQ8YruzOneqECRzwox"))
        )

        for container in controls_containers:
            links_element = container.find_elements(By.CSS_SELECTOR, "a.bloko-button")
            for link in links_element:
                href = link.get_attribute('href')
                if href:
                    link.click()
                    all_links.append(href)

        with open("links.txt", "w") as f:
            for link in all_links:

                f.write(link + '\n')
                print(link + '\n')

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    link_search = input("Link search: ")
    login_user()
    found_all_links(link_search)

    # Ссылка для вставки
# https://hh.ru/search/vacancy?text=Name%3A%28python+or+django+or+drf+or+backend+or+fastapi%29+and+DESCRIPTION%3A%28django+or+drf+or+fastapi%29&salary=&ored_clusters=true&enable_snippets=true&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line


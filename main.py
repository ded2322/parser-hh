from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
path = "https://hh.ru/search/vacancy?hhtmFrom=main&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&text=python+backend+developer&enable_snippets=true&L_save_area=true"
driver.get(path)

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
                all_links.append(href)

    with open("links.txt", "w") as f:
        for i in all_links:
            f.write(i+'\n')

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Закрытие браузера
    driver.quit()
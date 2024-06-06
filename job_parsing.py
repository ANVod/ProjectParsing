# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
driver = webdriver.Firefox()
# Если мы используем Chrome, пишем
# driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://tomsk.hh.ru/vacancies/programmist"

# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)

# Находим все карточки с вакансиями с помощью названия класса
# Названия классов берём с кода сайта
vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')

# Выводим вакансии на экран
print(vacancies)
# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for vacancy in vacancies:
    try:
        # Находим элементы внутри вакансий по значению
        # Находим названия вакансии
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
        # Находим названия компаний
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
        # Находим зарплаты
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
        # Находим ссылку с помощью атрибута 'href'
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
# Добавляем полученную информацию в список
        parsed_data.append([title, company, salary, link])

    # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
    except:
        print("произошла ошибка при парсинге")
        continue

# Закрываем подключение браузера
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])

    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)
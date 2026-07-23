![Project-logo](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/project-logo.png)
#### [EN](https://github.com/isachenko-andrii/streamlit-sales-dashboard/blob/main/README.md) | [UA](https://github.com/isachenko-andrii/streamlit-sales-dashboard/blob/main/README-UA.md) Цей матеріал також доступний англійською мовою.
---  
<div align="center">  
    
## Аналітичний дашборд продажів та прибутку<br>(Streamlit)   
  
</div>  
  
## Опис проєкту  
  
Інтерактивний аналітичний дашборд для дослідження продажів, прибутковості та ефективності дисконтної політики роздрібної мережі (Superstore Dataset).  

**Live Demo:** [Sales & Profit Analytics Dashboard](https://sales-and-profit-dashboard.streamlit.app/)  
  
## Мета проекту  
    
Цей проект створено як **практичну демонстрацію навичок побудови, оптимізації та деплою інтерактивних дата-додатків за допомогою фреймворку [Streamlit.io](https://streamlit.io/)**. 
Проект показує повний цикл роботи аналітика даних: від первинного аналізу (EDA) та написання модульного Python-коду до автоматизації хостингу веб-додатка в хмарі Streamlit Community Cloud.  

---
  
### Основні можливості:  
* **Інтерактивна фільтрація:** Діапазон дат, регіони, категорії та сегменти клієнтів з динамічним підрахунком відфільтрованих записів.  
* **Моніторинг KPI:** Виторг ($), Прибуток ($), Кількість замовлень, Середній чек ($) та Маржинальність (%).  
* **Аналітичні блоки:**  
  * Динаміка продажів та прибутку по місяцях (Plotly Line Chart).  
  * Аналіз продажів за категоріями та регіонами (Bar Chart + Donut Chart).  
  * Ранжування Топ-10 підкатегорій з автоматичним виявленням збиткових позицій.  
  * Scatter Plot залежності прибутку від знижки з підрахунком кореляції Пірсона.  
* **Експорт даних:** Перегляд інтерактивної таблиці та вивантаження відфільтрованого зрізу в CSV.  
  
---

## Технологічний стек

* **Мова програмування:** Python 3.11
* **Фреймворк веб-додатку:** Streamlit
* **Обробка та аналіз даних:** Pandas, NumPy
* **Інтерактивна візуалізація:** Plotly Express
* **Версіонування та деплой:** Git, GitHub, Streamlit Community Cloud

---

## Етапи реалізації проекту

Розробка проекту проходила у 3 ключові етапи:

### Етап 1: Написання коду та аналітична розробка (`app.py`)  
  
1. **Підготовка даних:** Очищення та приведення типів (конвертація дат, розрахунок агрегованих полів `Month`, `Delivery Days`).  
2. **Оптимізація швидкодії:** Застосування кешування Streamlit (`@st.cache_data`) для миттєвого завантаження даних при роботі з фільтрами.  
3. **Побудова UI/UX:** Створення зручної бічної панелі (Sidebar) з мультиселектами та індикаторами стану.  
4. **Інтеграція Plotly:** Налаштування кастомних кольорових шкал (`RdYlGn`), інтерактивних підказок та адаптивного розміру графіків.

![Writing code](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/ssd_1.png)  
  
### Етап 2: Версіонування та розміщення на GitHub  
  
1. Структуризація проекту (виділення папки `data/`, файлу залежностей `requirements.txt` та фіксація версії Python у `runtime.txt`).  
2. Створення Git-репозиторію та публікація коду на GitHub.  
3. Документування проекту у файлі `README.md`.  
  
![Publishing on Streamlit](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/ssd_2.png)  
  
### Етап 3: Публікація та деплой на Streamlit.io
  
1. Підключення GitHub-репозиторію до платформи **Streamlit Community Cloud**.  
2. Налаштування автоматичного деплою (CI/CD): додаток автоматично оновлюється при кожному новому комміті в гілку `main`.  
3. Перевірка стабільності роботи та коректності відображення візуалізацій у хмарі.  

![Hosting on GitHub](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/ssd_3.png) 
  
---  
 
## Структура проекту

**streamlit-sales-dashboard/** — каталог проєкту  
    ├── doc/ — технычне завдання   
    ├── data/ — дані проєкту  
    ├── img/ — збережені графіки та підсумкові таблиці  
    ├── app.py — файл з кодом проэкту  
    ├── requirements.txt — список бібліотек для запуску проєкту  
    ├── runtime.txt — .версія Python для Streamlit Cloud  
    ├── gitignore - шаблони ігнорування git  
    ├── LICENSE — MIT Ліцензія   
    ├── project-logo.png — обкладинка проекту  
    ├── README-UA.md  — опис проекту українською мовою   
    └── README.md — опис проекту англійською мовою     
  
## Як використовувати  
  
...  
    
## Контакти  
    
**Автор:** [Andrii Isachenko](https://isachenko-andrii.github.io)    
**Посада:** Junior Data Analyst  
**LinkedIn:** [Andrii Isachenko](https://www.linkedin.com/in/isachenko-andrii/)  
**E-mail:** andrii.isachenko@gmail.com   
  
## Подяки    
  
 * Дякую [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) за надання відкритого навчального датасета Superstore Sales, який є чудовою базою для відпрацювання навичок дослідницького аналізу даних (EDA) та бізнес-моделювання.  
 * Особлива подяка [Streamlit.io](https://streamlit.io/) за створення потужного, інтуїтивно зрозумілого open-source фреймворку та надання безкоштовної хмарної платформи Streamlit Community Cloud, що дозволяє швидко перетворювати Python-скрипти на повноцінні інтерактивні веб-додатки.  
  
---
  
**Статус проекту:** Виконано.  
**Ліцензія:** MIT License.  

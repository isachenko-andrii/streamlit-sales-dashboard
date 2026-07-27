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
* **(UPD: Багатомовність)**  
  
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
    ├── data/ — дані проєкту  
    ├── img/ — збережені графіки та підсумкові таблиці  
    ├── app.py — файл з кодом проэкту  
    ├── requirements.txt — список бібліотек для запуску проєкту  
    ├── runtime.txt — .фіксує версію Python для Streamlit Cloud  
    ├── gitignore - шаблони ігнорування git  
    ├── LICENSE — MIT Ліцензія   
    ├── project-logo.png — обкладинка проекту  
    ├── README-UA.md  — опис проекту українською мовою   
    └── README.md — опис проекту англійською мовою     
  
## Як використовувати 

Ознайомитись з функціоналом можно за посиланням  

**Live Demo:** [Sales & Profit Analytics Dashboard](https://sales-and-profit-dashboard.streamlit.app/)  

Для запуску на іншому аккаунті Streamlit Community Cloud потрібно виконати наступні дії:
  
**Попередні вимоги (Prerequisites)**  
  
Перед початком переконайся, що у тебе є:  
  
1. **Акаунт на GitHub**, на якому розміщено (або сфорковано) публічний репозиторій із проектом.  
2. **Акаунт на Streamlit Community Cloud** (авторизація відбувається через GitHub).  
3. У репозиторії наявні обов'язкові конфігураційні файли:  
   * `app.py` — головний скрипт додатка.  
   * `requirements.txt` — список Python-бібліотек та їх версій.  
   * `runtime.txt` — вказівка версії Python (наприклад, `python-3.11`).  
  
---  
  
**Покроковий алгоритм розгортання** 
  
**Крок 1. Підготовка GitHub-репозиторію**  
  
Залежно від того, де знаходиться оригінальний код, оберіть один із двох варіантів:  
  
* **Варіант A (Fork):** Якщо проект лежить у чужому/іншому GitHub-акаунті, зайди на сторінку репозиторію та натисни кнопку **Fork** у верхньому правому кутку.  
Це створить копію проекту у вашому власному GitHub-профілі.  
* **Варіант B (Transfer / Push):** Якщо ви створюєте новий репозиторій, завантажте туди файли проекту за допомогою Git:  

   <code>```bash  
  git init  
  git add .
  git commit -m "Initial commit for Streamlit Cloud deployment"  
  git branch -M main  
  git remote add origin [https://github.com/](https://github.com/)<YOUR_GITHUB_USERNAME>/<REPOSITORY_NAME>.git  
  git push -u origin main</code>  
  
**Крок 2. Авторизація на Streamlit Community Cloud**  
  
 - Перейдіть на сайт share.streamlit.io або streamlit.io.  
 - Натисніть Sign in (або Get started).  
 - Оберіть спосіб входу Continue with GitHub та авторизуйся під потрібним (новим) акаунтом GitHub.  
 - Надайте Streamlit необхідні дозволи (OAuth Access) для читання ваших GitHub-репозиторіїв.  
  
**Крок 3. Налаштування та деплой додатка (Create App)**  
  
У робочому просторі (Workspace) Streamlit Cloud натисніть кнопку New app (або Create app у правому верхньому кутку).  
У формі, що з'явилася, заповніть наступні поля:  
 * **Repository:** Оберіть зі списку свій GitHub-репозиторій (наприклад, username/sales-and-profit-dashboard).
 * **Branch:** Вкажіть основну гілку (зазвичай main або master).
 * **Main file path:** Вкажіть шлях до головного файлу додатка (наприклад, app.py).
 * **App URL (за бажанням):** Ви можете задати кастомний субдомен (наприклад, sales-and-profit-dashboard-new).  

**Автоматичне оновлення (CI/CD)**

Streamlit Community Cloud підтримує автоматичне оновлення. При внесенні будь-яких змін у код та виконанні push у гілку main на GitHub (git push origin main), дашборд оновиться в хмарі автоматично протягом 1-2 хвилин.  

**UPD !!!Важливо у св'язку з наявністю лімітів у безкоштовній версії хостінгу Streamlit Community Cloud за для демонстаці працездатності дашборду використано облегшений датасет superstore.csv**   
**повну версію можна завантажити на Kaggle за посиланням: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final**  
**для повноцінного використання просто заменіть полегшений файл superstore.csv на повний**  

**Скріншоти функціональних можливостей дашборда:**  
  
 - **Ключові показники ефективності**
![Key Performance Indicators](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/screenshots/ssd_1s.png)

 - **Динаміка продажу та прибутку по місяцях**  
  
![Monthly Sales and Profit Trend](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/screenshots/ssd_2s.png)  
  
 - Продажі за категоріями та регіонами  
  
![Category and Region](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/screenshots/ssd_3s.png)  

 - Топ-10 підкатегорій за прибутком

![Top 10 Sub-Categories by Profit](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/screenshots/ssd_4s.png)  

 - Вплив знижки на прибуток  
  
![Discount Impact on Profit](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/screenshots/ssd_5s.png)  
  
 - Детальні дані

![Detailed Data](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/screenshots/ssd_6s.png)  
  
 - Робота фільтрів  
  
![Filters](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/screenshots/ssd_7s.png)  
  
---  
    
## Контакти  
    
**Автор:** [Andrii Isachenko](https://isachenko-andrii.github.io)    
**Посада:** Junior Data Analyst  
**LinkedIn:** [Andrii Isachenko](https://www.linkedin.com/in/isachenko-andrii/)  
**E-mail:** andrii.isachenko@gmail.com   
  
## Подяки    
  
 * Дякую [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) за надання відкритого навчального датасета Superstore Sales, який є чудовою базою для відпрацювання навичок дослідницького аналізу даних (EDA) та бізнес-моделювання.  
 * Особлива подяка [Streamlit.io](https://streamlit.io/) за створення потужного, інтуїтивно зрозумілого open-source фреймворку та надання безкоштовної хмарної платформи Streamlit Community Cloud, що дозволяє швидко перетворювати Python-скрипти на повноцінні інтерактивні веб-додатки.  
  
---
  
**Статус проекту:** Виконано. Заплановані вдосконалення: багатомовність (**UPD** виконано), захист доступу паролем (**UPD** виконано окремим проектом)  
**Ліцензія:** MIT License.  
  

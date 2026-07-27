 ![Project-logo](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/project-logo.png)
#### [EN](https://github.com/isachenko-andrii/streamlit-sales-dashboard/blob/main/README.md) | [UA](https://github.com/isachenko-andrii/streamlit-sales-dashboard/blob/main/README-UA.md)  This material is also available in Ukrainian.  
---  
<div align="center">  
    
## Sales and profit analytics dashboard<br>(Streamlit)   
  
</div>  
  
## Project description  
  
Interactive analytical dashboard for researching sales, profitability, and effectiveness of a retail chain's discount policy (Superstore Dataset).  
  
**Live Demo:** [Sales & Profit Analytics Dashboard](https://sales-and-profit-dashboard.streamlit.app/)  
  
## Project goal   
    
This project is designed as a **practical demonstration of skills in building, optimizing, and deploying interactive data applications using the [Streamlit.io](https://streamlit.io/) framework**.  
The project shows the full cycle of data analytics work: from initial analysis (EDA) and writing modular Python code to automating web application hosting in the Streamlit Community Cloud.  
  
---  
  
### Main features:  
  
* **Interactive filtering:** Date range, regions, categories and customer segments with dynamic counting of filtered records.  
* **KPI monitoring:** Revenue ($), Profit ($), Number of orders, Average check ($) and Marginality (%).  
* **Analytical blocks:**  
* Sales and profit dynamics by month (Plotly Line Chart).  
* Sales analysis by category and region (Bar Chart + Donut Chart).  
* Ranking of Top 10 subcategories with automatic detection of unprofitable positions.  
* Scatter Plot of profit dependence on discount with calculation of Pearson correlation.  
* **Data export:** View interactive table and download filtered slice to CSV.  
* **(UPD: Multilingual)**  
  
---  
  
## Technology Stack  
  
* **Programming Language:** Python 3.11  
* **Web Application Framework:** Streamlit  
* **Data Processing and Analysis:** Pandas, NumPy  
* **Interactive Visualization:** Plotly Express  
* **Versioning and Deployment:** Git, GitHub, Streamlit Community Cloud  
  
---  

## Project Implementation Stages  
  
The project development took place in 3 key stages:  
  
### Stage 1: Code Writing and Analytical Development (`app.py`)  
  
1. **Data preparation:** Cleaning and type conversion (date conversion, calculation of aggregated fields `Month`, `Delivery Days`).  
2. **Performance optimization:** Using Streamlit caching (`@st.cache_data`) for instant data loading when working with filters.  
3. **UI/UX construction:** Creating a convenient sidebar with multiselects and status indicators.  
4. **Plotly integration:** Setting up custom color scales (`RdYlGn`), interactive tooltips, and adaptive chart size.  
  
![Writing code](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/ssd_1.png)  
  
### Stage 2: Versioning and hosting on GitHub  
  
1. Structuring the project (allocating the `data/` folder, the `requirements.txt` dependency file, and setting the Python version in `runtime.txt`).  
2. Creating a Git repository and publishing the code on GitHub.  
3. Documenting the project in the `README.md` file.
   
![Publishing on Streamlit](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/ssd_2.png)  
  
### Stage 3: Publishing and deploying on Streamlit.io  
  
1. Connecting the GitHub repository to the **Streamlit Community Cloud** platform.  
2. Setting up automatic deployment (CI/CD): the application is automatically updated with each new commit to the `main` branch.  
3. Checking the stability of the operation and the correctness of the visualizations displayed in the cloud.  
  
![Hosting on GitHub](https://github.com/isachenko-andrii/streamlit-sales-dashboard/raw/main/img/ssd_3.png) 
  
---  
  
## Project structure  
  
**streamlit-sales-dashboard/** — project directory  
├── data/ — project data  
├── img/ — saved graphs and summary tables  
├── app.py — file with project code  
├── requirements.txt — list of libraries to run the project  
├── runtime.txt — .fixes the Python version for Streamlit Cloud  
├── gitignore - git ignore templates  
├── LICENSE — MIT License  
├── project-logo.png — project cover  
├── README-UA.md — project description in Ukrainian  
└── README.md — project description in English  
  
## How to use  
  
You can familiarize yourself with the functionality at the link  
  
**Live Demo:** [Sales & Profit Analytics Dashboard](https://sales-and-profit-dashboard.streamlit.app/)  
  
To run on another Streamlit Community Cloud account, you need to perform the following steps:  
  
**Prerequisites**  
  
Before you start, make sure you have:  
  
1. **A GitHub account** on which a public repository with the project is hosted (or forked).  
2. **A Streamlit Community Cloud account** (authorization is done via GitHub).  
3. The repository contains mandatory configuration files:  
* `app.py` — the main script of the application.  
* `requirements.txt` — a list of Python libraries and their versions.  
* `runtime.txt` — an indication of the Python version (for example, `python-3.11`).
  
---   
  
**Step-by-step deployment algorithm**  
  
**Step 1. Prepare the GitHub repository**  
  
Depending on where the original code is located, choose one of two options:  
  
* **Option A (Fork):** If the project is in someone else's/different GitHub account, go to the repository page and click the **Fork** button in the upper right corner.  
This will create a copy of the project in your own GitHub profile.  
* **Option B (Transfer / Push):** If you are creating a new repository, upload the project files there using Git:  
  
   <code>```bash  
  git init  
  git add .
  git commit -m "Initial commit for Streamlit Cloud deployment"  
  git branch -M main  
  git remote add origin [https://github.com/](https://github.com/)<YOUR_GITHUB_USERNAME>/<REPOSITORY_NAME>.git  
  git push -u origin main</code>  
  
**Step 2. Authorization on Streamlit Community Cloud**  
  
- Go to share.streamlit.io or streamlit.io.  
- Click Sign in (or Get started).  
- Choose the Continue with GitHub login method and authorize with the desired (new) GitHub account.  
- Grant Streamlit the necessary permissions (OAuth Access) to read your GitHub repositories.  
  
**Step 3. Configure and deploy the application (Create App)**  
  
In the Streamlit Cloud workspace (Workspace), click the New app button (or Create app in the upper right corner).  
In the form that appears, fill in the following fields:  
  
* **Repository:** Select your GitHub repository from the list (for example, username/sales-and-profit-dashboard).  
* **Branch:** Specify the main branch (usually main or master).  
* **Main file path:** Specify the path to the main application file (for example, app.py).  
* **App URL (optional):** You can specify a custom subdomain (e.g. sales-and-profit-dashboard-new).  
  
**Automatic Updates (CI/CD)**  
  
Streamlit Community Cloud supports automatic updates. When you make any changes to the code and push to the main branch on GitHub (git push origin main), the dashboard will be updated in the cloud automatically within 1-2 minutes.  
  
**UPD !!!It is important due to the presence of limits in the free version of Streamlit Community Cloud hosting, a lightweight superstore.csv dataset was used to demonstrate the functionality of the dashboard**
**the full version can be downloaded on Kaggle at the link: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final**
**for full use just replace the lightweight superstore.csv file with the full one**  
  
---  
    
## Contacts  
  
**Author:** [Andrii Isachenko](https://isachenko-andrii.github.io)  
**Position:** Junior Data Analyst  
**LinkedIn:** [Andrii Isachenko](https://www.linkedin.com/in/isachenko-andrii/)  
**E-mail:** andrii.isachenko@gmail.com  
  
## Acknowledgements  
  
* Thanks to [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) for providing the open training dataset Superstore Sales, which is an excellent base for practicing exploratory data analysis (EDA) and business modeling skills.  
* Special thanks to [Streamlit.io](https://streamlit.io/) for creating a powerful, intuitive open-source framework and providing a free cloud platform Streamlit Community Cloud, which allows you to quickly turn Python scripts into full-fledged interactive web applications.  
  
---  
  
**Project status:** Completed. Planned improvements: multilingual (**UPD** completed), password protection (**UPD** completed as a separate project)  
**License:** MIT License.  
  

# 🌦 Weather Data Dashboard

An interactive **Streamlit** application for visualizing weather data from a CSV file.  
It provides quick and clear insights into **temperature trends**, **humidity distribution**, and **rainfall patterns** using simple visualizations.

---

## ✨ Features

- 📂 **CSV Upload** — Quickly upload your dataset for instant visualization.  
- 📈 **Temperature Line Chart** — Trend of maximum temperature (first 20 records).  
- 💧 **Humidity Histogram** — Frequency distribution of humidity at 9 AM.  
- 🌧 **Rainfall Bar Chart** — Rainfall values for the first 20 records.  
- 🔍 **Data Preview** — Scrollable and interactive table to view the dataset.

---

## 🛠 Tech Stack

- [Python](https://www.python.org/) — Core programming language  
- [Streamlit](https://streamlit.io/) — Web app framework  
- [Pandas](https://pandas.pydata.org/) — Data manipulation  
- [Matplotlib](https://matplotlib.org/) — Data visualization  

---

## 🚀 Installation & Usage

```bash
# 1️⃣ Clone this repository
git clone https://github.com/TanviTater/WeatherDataDashboard.git
cd WeatherDataDashboard

# 2️⃣ Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt
# If requirements.txt is not available:
pip install streamlit pandas matplotlib
pip freeze > requirements.txt

# 4️⃣ Run the application
streamlit run main.py

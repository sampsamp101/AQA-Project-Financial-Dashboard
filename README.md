# AQA Project – Financial Dashboard

This simple project is part of an assignment to build a financial dashboard. It uses:

- **Flask** to expose financial data through a REST API
- **Dash** and **Plotly** for building interactive visuals
- **Dash Mantine Components** for a modern UI
-  Data CSV Reference: https://www.kaggle.com/datasets/franoisgeorgesjulien/s-and-p-500-companies-with-financial-information

---

## 🔧 How It Works

### Backend (Flask):
- `main.py` loads data from `financial_data.csv`
- Provides 3 API endpoints:
  - `/Sector` – returns a list of unique sectors
  - `/EBITDA?Sector=...` – returns EBITDA values for that sector
  - `/Download` - Download the raw CSV file 

### Frontend (Dash):
- `dashboard.py` fetches sectors via the API
- Allows user to select sectors using a multi-select component
- Displays a pie chart showing total EBITDA per sector
- Includes a Download button for CSV
---

## 💻 Setup & Run

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/AQA-Project-Financial-Dashboard.git
cd AQA-Project-Financial-Dashboard
```

### 2. 🧪 (Optional) Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate 
```


### 3. 📦 Install Dependencies

```bash
pip install flask dash pandas plotly dash-mantine-components
```

### 4. Run the Flask Backend

```bash
python main.py
```
Visit: http://127.0.0.1:5000/Sector to test

### 5. Run the dashboard (in another terminal)

```bash
python dashboard.py
```

Visit: http://127.0.0.1:8050 to test




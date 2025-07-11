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
- Provides 2 API endpoints:
  - `/Sector` – returns a list of unique sectors
  - `/EBITDA?Sector=...` – returns EBITDA values for that sector

### Frontend (Dash):
- `dashboard.py` fetches sectors via the API
- Allows user to select sectors using a multi-select component
- Displays a pie chart showing total EBITDA per sector

---

## 💻 How to Run

### 1. Install dependencies

```bash
pip
 install flask dash pandas plotly dash-mantine-components
```

### 2. Start the API Server

```bash
python main.py
```
Visit: http://127.0.0.1:5000/Sector to test

### 3. Run the dashboard (in an seperate Terminal)

```bash
python dashboard.py
```

Visit: (Visit: http://127.0.0.1:8050) to test




import requests
import dash
from dash import html, dcc, Input, Output
import dash_mantine_components as dmc
import plotly.express as px
from dash_mantine_components import MantineProvider

# Step A: Query sectors from your Flask API
SECTOR_API = "http://127.0.0.1:5000/Sector"
EBITDA_API = "http://127.0.0.1:5000/EBITDA"

try:
    response = requests.get(SECTOR_API)
    _sectors = response.json() if response.status_code == 200 else []
except Exception as e:
    print(f"API error: {e}")
    _sectors = []

# Step B: Function to get EBITDA for a sector
def get_ebitda(sector):
    r = requests.get(EBITDA_API, params={"Sector": sector})
    if r.status_code == 200:
        return sum(r.json())  # Total EBITDA for sector
    return 0

# Step C + D: Create dashboard
app = dash.Dash(__name__)

app.layout = MantineProvider([
    html.H1("EBITDA Distribution by Sector"),

    dmc.MultiSelect(
        id="sector-select",
        label="Choose Sectors",
        data=_sectors,
        placeholder="Select one or more sectors",
        clearable=True
    ),

    dcc.Graph(id="ebitda-pie")
])

# Step D3: Callback to update pie chart
@app.callback(
    Output("ebitda-pie", "figure"),
    Input("sector-select", "value")
)
def update_pie_chart(selected_sectors):
    if not selected_sectors:
        return px.pie(names=[], values=[], title="No sectors selected")

    data = {sector: get_ebitda(sector) for sector in selected_sectors}

    fig = px.pie(
        names=list(data.keys()),
        values=list(data.values()),
        title="EBITDA Distribution by Sector"
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)

# Live Stock Dashboard

A Dockerized real-time stock dashboard built with Python and Streamlit. Fetches live data using the yfinance API and displays:
- Real-time prices and percentage changes
- Color-coded gain/loss
- Historical charts (7D, 1M, 1Y)
- Auto-refreshes every 30 seconds

## Folder Structure
```
stock-dashboard/
  ├── app/
  │     ├── dashboard.py
  │     └── requirements.txt
  └── Dockerfile
```

## Installation & Running

### Option 1: Run Locally with Python

**It is strongly recommended to use a Python virtual environment to avoid dependency conflicts.**

1. **Navigate to the app directory:**
   ```
   cd app
   ```
2. **Create and activate a virtual environment:**
   - On Windows (CMD):
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - On PowerShell:
     ```
     python -m venv venv
     venv\Scripts\Activate.ps1
     ```
   - On Git Bash/WSL:
     ```
     python -m venv venv
     source venv/Scripts/activate
     ```
   - On **Linux or MacOS**:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **Install dependencies from requirements.txt:**
   ```
   pip install -r requirements.txt
   ```
4. **Start the Streamlit app:**
   ```
   streamlit run dashboard.py
   ```
5. **Open your browser and go to:**
   [http://localhost:8501](http://localhost:8501)

---

### Note on Dependencies
All required libraries are listed in `requirements.txt`. Make sure your virtual environment is activated before running the `pip install -r requirements.txt` command.

---

### Option 2: Run with Docker
1. **Navigate to the project root:**
   ```
   cd stock-dashboard
   ```
2. **Build the Docker image:**
   ```
   docker build -t stock-dashboard .
   ```
3. **Run the Docker container:**
   ```
   docker run -p 8501:8501 stock-dashboard
   ```
4. **Open your browser and go to:**
   [http://localhost:8501](http://localhost:8501)

---

## Features
- Real-time stock prices for major tickers (AAPL, VOO, VTI, etc.)
- Percentage change and color-coded gain/loss
- Historical performance charts (7D, 1M, 1Y)
- Auto-refresh every 30 seconds

## Requirements
- Python 3.8+
- Or Docker

---

## License
MIT

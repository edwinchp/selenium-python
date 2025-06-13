# Pytest + Selenium Framework (Python)

This project demonstrates how to use **Pytest** with **Selenium WebDriver** in Python. It includes automatic WebDriver management with `webdriver-manager` and generates test reports in HTML format using `pytest-html`.

## 🛠 Requirements

- Python 3.7+
- Google Chrome browser installed
- pip (comes with Python)
- `virtualenv` (optional but recommended)

## 🐍 Create and activate a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
pytest -m login --html=reports/report.html
```

Run with specific browser (Chrome is default)
```bash
pytest -m login --html=reports/report.html --browser="firefox"
```

Run in parallel
```bash
pytest -m login --html=reports/report.html -n=2
```
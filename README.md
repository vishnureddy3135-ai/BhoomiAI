# BhoomiAI — Smart Farming Companion

A Flask-based hackathon website starter with six farmer-support modules:
CropDoctor, SmartJal, FarmConnect, AgriAlert, HarvestGuard, and AI Assistant.

## 1. Requirements
- Python 3.10 or newer (Python 3.11 recommended)
- VS Code or another code editor
- Internet connection for deployment

## 2. Run locally (Windows)
Open this folder in VS Code. In the terminal:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python app.py
```

Open http://127.0.0.1:5000

If `py -3.11` is unavailable, use `python -m venv .venv`.

## 3. Run locally (macOS / Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

## 4. Deploy
This project includes a `Procfile` for common Python hosting platforms.
1. Create a GitHub repository and upload the project files (do not upload `.env`).
2. Create a new Web Service on a Python-compatible host such as Render.
3. Connect the GitHub repository.
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Deploy, then open the public URL provided by the host.

Hosting dashboards change over time; follow the platform's current prompts. Add environment variables in the hosting dashboard, not in source code.

## 5. Current prototype status
- Responsive dashboard and six module screens are included.
- Assistant and crop-check endpoints return safe starter/demo guidance.
- Crop image preview is local in the browser; images are not uploaded or diagnosed by an AI model.
- Weather, live mandi prices, verified buyers, maps, user accounts, database, payments, and IoT sensors are NOT connected yet.
- Demo market values must not be treated as current prices.
- Do not use sample advice as a substitute for an agricultural expert or product label.

## 6. Before public launch
- Replace the demo assistant with a properly configured AI provider and validate agricultural answers.
- Integrate an official/reliable weather source and a trusted market-price source.
- Add authentication, database, privacy notice, abuse protection, logging, and backups if storing farmer data.
- Validate all pesticide/fertilizer advice with qualified agronomists and local regulations.
- Never expose API keys in frontend JavaScript or commit `.env` to GitHub.

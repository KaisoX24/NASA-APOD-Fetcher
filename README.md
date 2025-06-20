# 🌌 NASA APOD Fetcher

A simple Python script that fetches the **Astronomy Picture of the Day (APOD)** from NASA's API based on a user-input date. It also gives you the option to download the image locally.

---

## 📌 Features

- 🔭 Fetches NASA's APOD (title, image, explanation, and date)
- 📅 Accepts user-defined date input (YYYY-MM-DD)
- 🌐 Uses official NASA public API
- 💾 Optional image download functionality
- ✅ Handles errors and invalid dates gracefully

---

## ⚙️ Tech Stack

| **Technology** | **Purpose**                                      |
|----------------|--------------------------------------------------|
| Python         | Core programming language                        |
| `requests`     | HTTP client to make API calls                    |
| NASA APOD API  | Data source (https://api.nasa.gov)               |
| `os`           | Fetch environment variable for API key           |

---

## 🔐 API Key Setup

You need a **NASA API key** to use the script.  
Get one from: [https://api.nasa.gov](https://api.nasa.gov)

---
## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KaisoX24/NASA-APOD-Fetcher.git
cd NASA-APOD-Fetcher
```
### 2. Install Dependencies

```bash
pip install requests
```
### 3. Set Up .env
Create a .env file in the root directory and add your NASA_API_KEY:
```bash
NASA_API_KEY=your_api_key_here
```
### 4. Run the Script
```bash
python main.py
```
---
## 🧑‍💻 Author
Developed by Pramit Acharjya
---
## 🪪 License
MIT License — free to use, modify, and distribute.

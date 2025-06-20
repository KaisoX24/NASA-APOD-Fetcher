import requests
import os
from google.adk.agents import Agent

API_KEY = os.getenv("NASA_API_KEY")
APOD_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

def fetch_nasa_apod(date):
    try:
        params = {
            "api_key": API_KEY,
            "date": date  
        }
        response = requests.get(APOD_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "title": data.get("title"),
                "explanation": data.get("explanation"),
                "url": data.get("url"),
                "date": data.get("date")
            }
        else:
            return {"error": response.text}
    except Exception as e:
        print('There is no image for this date.')

def download_image(image_url, filename):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image saved as {filename}")
    else:
        print("Failed to download the image.")


if __name__ == "__main__":
    date= input("Enter the date (YYYY-MM-DD) for NASA APOD: ")
    apod = fetch_nasa_apod(date)
    if apod:
        print(f"Title: {apod['title']}")
        print(f"Date: {apod['date']}")
        print(f"URL: {apod['url']}")
        print(f"Explanation: {apod['explanation']}")
        ask = input("Do you want to download the image? (yes/no): ").strip().lower()
        if ask == 'yes':
            print("Downloading image...")
            download_image(apod['url'], f"apod_{date}.jpg")
        else:
            print("Image download skipped.")
    else:
        print("Failed to fetch NASA APOD.")
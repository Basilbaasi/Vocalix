import os
import time
import wikipedia
import webbrowser
import requests
from datetime import datetime
from Vocalix.core import speak
from Vocalix.config import API_KEY, BASE_URL
from AppOpener import open as open_app, close as close_app

# ─────────────────────────────────────────────
#  AI AND WIKIPEDIA
# ─────────────────────────────────────────────

def model(question):
    invoke_url = f"{BASE_URL}/chat/completions"
    stream = True

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "text/event-stream" if stream else "application/json"
    }

    payload = {
        "model": "google/gemma-3n-e4b-it",
        "messages": [{"role": "user", "content": question}],
        "max_tokens": 512,
        "temperature": 0.2,
        "top_p": 0.7,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "stream": stream
    }

    response = requests.post(invoke_url, headers=headers, json=payload, stream=True)

    response_text = ""
    try:
        for line in response.iter_lines():
            if line:
                decoded = line.decode("utf-8")
                if decoded.startswith("data: "):
                    content = decoded.removeprefix("data: ").strip()
                    if content != "[DONE]":
                        import json
                        data = json.loads(content)
                        delta = data.get("choices", [{}])[0].get("delta", {})
                        if "content" in delta:
                            response_text += delta["content"]
    except Exception as e:
        print("Streaming error:", e)
        speak("Sorry, an error occurred while processing the response.")

    return response_text.replace("*", " ")

def search_wikipedia(query: str):
    query=query.lower()
    query = query.replace("wikipedia", "").strip()
    speak("Searching Wikipedia...")
    try:
        summary = wikipedia.summary(query, sentences=2)
        #print(summary)
        speak(summary)
    except Exception as e:
        print(f"Wikipedia Error: {e}")
        speak("Sorry, I couldn't find anything useful.")

def answer_question_short(question: str):
    question = question.replace("Vocalix", "").strip()
    try:
        response_text = model(question + " in short")
        #print(response_text)
        speak(response_text)
    except Exception as e:
        print("AI Error (short):", e)
        speak("I'm sorry, I couldn't find an answer.")

def chat():
    while True:
        question = input("enter for ai help :  ")
        try:
            response_text = model(question)
            #print("result:\n\n\n", response_text)
            speak("answer")
            p = input("\n\n\nREAD Y/N : ")
            if p.lower() == "y":
                speak(response_text)
            else:
                print(response_text)
        except Exception as e:
            print("An error occurred:", e)
            speak("I'm sorry, I couldn't find an answer.")

def answer_question_full(question: str):
    question = question.replace("Vocalix", "").strip()
    try:
        response_text = model(question)
        print("result:\n\n\n", response_text)
        speak(response_text)
    except Exception as e:
        print("AI Error (full):", e)
        speak("I'm sorry, I couldn't find an answer.")


# ─────────────────────────────────────────────
#  OPEN/CLOSE APPS BY NAME
# ─────────────────────────────────────────────

def control_apps(command: str):
    command = command.lower()
    apps = {
        "youtube": "youtube",
        "whatsapp": "whatsapp",
        "instagram": "instagram",
        "telegram": "telegram",
        "vlc": "vlc media player",
        "media player": "media player",
        "vs": "visual studio code",
        "store": "microsoft store",
        "settings": "settings",
        "notes": "onenote",
        "lightroom": "adobe lightroom",
        "photoshop": "adobe photoshop",
        "pc manager": "pc manager",
    }

    for key, app in apps.items():
        if f"open {key}" in command:
            open_app(app)
            speak(f"Opening {key}")
            return
        elif f"close {key}" in command:
            close_app(app)
            speak(f"Closing {key}")
            return

    if any(kw in command for kw in ["exit", "close", "get lost", "poda"]):
        speak("Okay then. Bye sir.")
        close_app("python")


# ─────────────────────────────────────────────
#  WEB SEARCH
# ─────────────────────────────────────────────

def open_website(query: str):
    query = query.replace("in web", "").replace("on web", "").strip()
    url = f"https://www.bing.com/search?q={query}"
    webbrowser.open(url)
    speak("Searching the web.")

# ─────────────────────────────────────────────
#  CUSTOM FILE/FOLDER SHORTCUTS
# ─────────────────────────────────────────────

def open_path(query: str):
    known_paths = {
        "open yt": "E:\\Yutb download",
        "open edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "open movies": "D:\\movies",
        "open downloads": "C:\\Users\\Admin\\Downloads",
        "open premiere": "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2023",
    }

    for trigger, path in known_paths.items():
        if trigger in query:
            try:
                os.startfile(path)
                speak("Opening...")
                return
            except Exception as e:
                print(f"Failed to open {path}: {e}")
                speak("Unable to open the specified path.")
                return

# ─────────────────────────────────────────────
#  TIME + IDENTITY
# ─────────────────────────────────────────────

def tell_time():
    current_time = datetime.now().strftime("%I:%M:%S")
    speak(f"Sir, the time is {current_time}")

def respond_identity():
    speak("I am Vocalix AI, a personal assistant for Basil. I can open apps, search the web, and answer your questions.")

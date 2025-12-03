
from Vocalix.core import *
from Vocalix.commands import *

def greet():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning, sir.")
    elif 12 <= hour < 18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")
    speak("Welcome back.")

if __name__ == "__main__":
    greet()
    while True:
        print("\n1) Speak \033[1mCHAT\033[0m for a chat version\n2) For searching web specify that like \033[1mIN WEB\033[0m in web\n3) Include \033[1mVocalix\033[0m in speach for AI answer\n4) Include \033[1mVocalix FULL\033[0m in speach for AI answer in detail\n5) Include \033[1mOPEN\033[0m for opening apps like open instagram \n")
        query = listen()
        if query == "none":
            continue

        if 'wikipedia' in query:
            search_wikipedia(query)
            
        elif 'on web' in query or 'in web' in query:
            open_website(query)

        elif 'Vocalix' in query:
            #if 'full' in query:
            if 'full' in query:
                answer_question_full(query)
            else:
                answer_question_short(query)

        elif 'sleep' in query:
            speak("Sleeping for 5 minutes...")
            import time
            time.sleep(300)

        elif 'chat' in query:
            chat()

        elif any(k in query for k in ['open', 'close']):
            control_apps(query)


        elif 'open yt' in query or 'open movies' in query or 'open edge' in query:
            open_path(query)

        elif 'time' in query:
            tell_time()

        elif 'your name' in query or 'who are you' in query:
            respond_identity()

        elif any(exit_word in query for exit_word in ['exit', 'get lost']):
            speak("Okay, goodbye sir.")
            break

import tkinter as tk
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from bs4 import BeautifulSoup
import random
import subprocess
import datetime
from datetime import date
import openai
import os
import time
import json
import pyjokes
import imaplib
#from github import Github

# Create a root window
root = tk.Tk()

# Hide the root window
root.withdraw()

openai.api_key = ''

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

#access_token = "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"
#repo_owner = "Apsan1"

awake_quotes = ["Was a great nap!, How can I help?","What's up?", "Help Here", "How are things?", "How's your day going?", "How's your day?", "How are you doing?",
                  "How are you?", "What's happening?", "What's going on?", "What's new?", "What's the good word?", "Rise and shine! Time to wake up and embrace the day. Remember, life's too short to sleep through all the fun!"
                  ]
greeting_quotes = ["Hi", "Hello", "Namaste", "Nahmaskar", "Darśshan Huhjur lai", "Konichiwa"]
help_quotes = ["I am here to help you", "I am here to assist you", "I am here to help you out", "I am here to assist you out",
                "I am here to help you with your tasks", "I am here to assist you with your tasks",
                "I can give you company"]
bye_quotes = ['See you soon', 'shutting down', 'bye bye', 'see you later', 'see you soon', 'have a nice day', 'enjoy your time']
gg_quotes = ['Happy Gaming', 'Enjoy your game',
            "Every game is an opportunity to level up and become a better player.",
            "In the game of life, play with passion, perseverance, and a hunger for success.",
            "The true joy of gaming lies not only in winning but in the journey and the challenges it brings.",
            "Game on! Embrace the thrill of competition and strive to be the best.",
            "Remember, it's not about how many times you fall in the game, but how many times you get back up and keep playing.",
            "In gaming and in life, every setback is an opportunity for a comeback.",
            "A game is not just about pixels and controllers; it's a chance to explore new worlds and create unforgettable memories.",
            "The best players don't just play the game; they immerse themselves in it and leave a mark.",
            "In the game of success, the only limit is the one you set for yourself.",
            "Mastering a game takes time, practice, and a willingness to learn from both victories and defeats.",
            "Play with sportsmanship, respect, and a spirit of camaraderie. It's not just about winning; it's about the experience.",
            "The beauty of gaming lies in the connections we make, the friendships we forge, and the shared experiences we cherish.",
            "Don't be afraid to take risks, try new strategies, and push beyond your comfort zone. Greatness comes from daring to be different.",
            "Remember, it's not just about the final score; it's about the memories, the laughter, and the friendships formed along the way.",
            "In the game of life, the true winners are those who find joy in every moment and inspire others to do the same.",
            "When the game gets tough, stay focused, stay determined, and believe in your ability to overcome any challenge.",
            "Gaming is not just a hobby; it's an art form that allows us to unleash our creativity and imagination.",
            "Celebrate every achievement, no matter how small. Each milestone is a testament to your growth and progress.",
            "The game may change, but the passion and love for gaming remain constant.",
            "Embrace the game of life with a childlike wonder, curiosity, and a thirst for adventure.",
            "In the game of success, there are no shortcuts. It's the dedication, hard work, and perseverance that lead to victory.",
            ]
good_morning_quotes = ['Good Morning', 'Good Morning, Captain boat is ready', 'Good Morning, Sir', 'System online and ready to serve you',
                       "Rise and shine! It's a brand new day filled with endless possibilities.",
                        "Sending you a big smile and lots of love to start your day off right. Good morning!",
                        "Wake up with determination, go to bed with satisfaction. Have a fantastic morning!",
                        "Every morning is a chance at a new beginning. Embrace it with open arms and a grateful heart.",
                        "May your morning be as bright and beautiful as your smile. Good morning!",
                        "Today is a gift. Don't forget to unwrap it and make the most of every moment. Good morning!",
                        "Wishing you a day filled with laughter, joy, and all the goodness life has to offer. Good morning!",
                        "Good morning! May your day be filled with positivity, kindness, and success in all your endeavors.",
                        "Rise above the challenges, seize the opportunities, and make today the best day of your life. Good morning!",
                        "Here's to a morning filled with happy thoughts, warm hugs, and a cup of your favorite coffee. Enjoy!",
                        "Waking up is like being reborn every day, except instead of a delivery room, you have a cozy bed, and instead of crying, you can start the day with laughter and a cup of coffee! haha good morning!"
                       ]
good_afternoon_quotes = [
    "Good afternoon! May the rest of your day be as beautiful as the morning was.",
    "Wishing you a delightful afternoon filled with happiness and success.",
    "Take a break, breathe in the fresh air, and enjoy the beauty of this afternoon.",
    "Sending you warm wishes for a peaceful and productive afternoon. Make it count!",
    "Good afternoon! May your afternoon be filled with pleasant surprises and wonderful moments.",
    "Take a moment to pause and appreciate the beauty of this afternoon. Enjoy every moment.",
    "May your afternoon be filled with sunshine, laughter, and sweet moments to cherish.",
    "Sending you positive vibes and energy to carry you through the afternoon.",
    "Good afternoon! Remember to take some time for yourself and recharge.",
    "Wishing you a lovely afternoon filled with love, joy, and good company.",
    "Embrace the beauty of this afternoon and let it inspire you to accomplish great things.",
    "As the sun shines brightly, may your afternoon be filled with positivity and success.",
    "Take a deep breath and let go of any stress. It's time to enjoy a peaceful afternoon.",
    "Good afternoon! May your day continue to unfold with endless possibilities and happiness.",
    "Wishing you a vibrant and productive afternoon. Keep shining!",
    "Pause for a moment and appreciate the beauty of this afternoon. Life is filled with wonders.",
    "Sending you warm afternoon wishes filled with love, peace, and contentment.",
    "May the afternoon bring you closer to your goals and dreams. Keep pushing forward.",
    "Good afternoon! Let go of what didn't go right in the morning and embrace the possibilities of the afternoon.",
    "Take a short break, enjoy a cup of tea, and recharge yourself for the rest of the day.",
    "Sending you rays of positivity and motivation to make this afternoon a successful one.",
    "Good afternoon! May your afternoon be filled with laughter, good conversations, and memorable moments.",
    "Wishing you a peaceful afternoon where all your worries and stress fade away.",
    "As the day progresses, may your energy and enthusiasm for life remain high. Have a fantastic afternoon!"
]
good_evening_quotes = [
    "Good evening! May the setting sun take down all your sufferings with it and make you hopeful for a new day.",
    "Good evening! May this beautiful evening fill your heart with hope and happiness.",
    "May the setting sun take away all your worries and concerns and fill your evening with joy and contentment.",
    "Good evening! Wishing you a relaxing and peaceful evening ahead.",
    "As the day comes to a close, may your evening be filled with joy and contentment.",
    "Sending you warm wishes for a beautiful and pleasant evening.",
    "May your evening be as lovely as the sunset and as peaceful as the moonlit night.",
    "Good evening! Take a moment to appreciate the beauty of this evening and count your blessings.",
    "Wishing you a delightful evening filled with laughter, good company, and beautiful moments.",
    "Embrace the serenity of this evening and let it rejuvenate your mind, body, and soul.",
    "May your evening be filled with happiness, love, and cherished memories.",
    "Sending you positive vibes and good energy for a fantastic evening ahead.",
    "Good evening! Remember to take some time for yourself and do something that brings you joy.",
    "As the day bids farewell, may your evening be filled with peace and tranquility.",
    "Wishing you a calm and refreshing evening that sets the stage for a peaceful night's rest.",
    "Enjoy the little moments of this evening and create beautiful memories to cherish.",
    "Good evening! May the stars shine brightly on your path and guide you to success.",
    "Take a deep breath and let go of any worries. It's time to relax and unwind in the evening.",
    "Wishing you a serene evening where you can unwind and find solace in the stillness.",
    "May your evening be a perfect blend of relaxation, joy, and fulfillment.",
    "Good evening! Reflect on the blessings of the day and look forward to a brighter tomorrow.",
    "Take a stroll, watch the sunset, and let the beauty of the evening inspire you.",
    "Sending you warm hugs and positive thoughts for a cozy and peaceful evening.",
    "Wishing you an evening filled with pleasant surprises and delightful moments.",
    "Good evening! May your evening be as wonderful as your smile.",
    "As the day draws to a close, may your evening be filled with gratitude and inner peace.",
    "Take a break from the busyness of life and enjoy a tranquil evening of relaxation.",
    "Sending you good vibes and blessings for a beautiful and memorable evening.",
    "Good evening! May your evening be filled with laughter, love, and happiness."
]
good_night_quotes = [

    "Goodnight! Rest your mind, body, and soul, and wake up refreshed to conquer the world.",
    "As you lay down to sleep, remember that tomorrow holds new opportunities and endless possibilities. Goodnight!",
    "Wishing you a peaceful and restful night's sleep. May you wake up with renewed energy and determination.",
    "Goodnight! Believe in yourself and your dreams. Tomorrow is another chance to make them a reality.",
    "May your dreams be filled with inspiration and your sleep be deep and restful. Goodnight!",
    "As the day ends, take a moment to appreciate how far you've come. Rest well and dream big. Goodnight!",
    "Close your eyes and imagine a brighter future. Sleep tight and wake up ready to make it a reality. Goodnight!",
    "Wishing you a night filled with dreams that ignite your passion and fuel your drive. Goodnight!",
    "Even the longest journeys start with a single step. Rest well tonight and prepare for a new day of progress. Goodnight!",
    "As you sleep, let go of any doubts or fears. Embrace the power within you and wake up ready to achieve greatness. Goodnight!",
    "Goodnight! Remember that every night is a chance to recharge and wake up with a fresh perspective.",
    "As the stars twinkle above, know that you are capable of shining just as brightly. Sleep well and dream big. Goodnight!",
    "Wishing you a peaceful night's sleep filled with dreams that inspire and motivate you. Goodnight!",
    "Goodnight! Rest your body, but never let your dreams rest. Chase them with passion and determination.",
    "As you drift off to sleep, remember that tomorrow is a blank canvas waiting for your masterpiece. Goodnight!",
    "Close your eyes, relax your mind, and visualize the success that awaits you. Sleep tight and dream big. Goodnight!",
    "May your dreams be filled with visions of success, happiness, and fulfillment. Goodnight!",
    "Goodnight! Tomorrow is a new day, a fresh start, and another opportunity to make your dreams come true.",
    "Rest well tonight, for tomorrow you will rise and continue your journey towards greatness. Goodnight!",
    "As the night envelops you, let go of the challenges of today and embrace the promises of tomorrow. Goodnight!",
    "Wishing you a night filled with peace, clarity, and the motivation to chase your dreams. Goodnight!"
]
howareyou_quotes = ['I am excited to help you out', 'I am excited to help you', 'I am excited to assist you', 'I am excited to assist you out', 'I am excited to help you with your tasks', 'I am excited to assist you with your tasks',
                     'I am doing great. I am excited to help you out', 'I am doing great. I am excited to help you', 'I am doing great. I am excited to assist you', 'I am doing great. I am excited to assist you out', 
                     'I am doing great. I am excited to help you with your tasks', 'I am doing great. I am excited to assist you with your tasks', 'Lovely, I am ready for tasks today', 'Robotically, Fine. Wait I am always fine.',
                     'Not getting paid, joking haha']

def introduce():
    speak("I am Athena. I am still developing and for now, I am able to do some general tasks which could save your time and also motivate you. Feel free to ask me anything.")

def greeting():
    random_greeting = random.choice(greeting_quotes)
    random_help = random.choice(help_quotes)
    speak(f"{random_greeting}, {random_help}.")

def handle_greeting(command):
    if 'meet my' in command:
        greet = command.replace('meet my', '')
        speak(f"Hello {greet}, how are you?")
    elif 'say hi to my' in command:
        greet = command.replace('say hi to my ', '')
        speak(f"Hello {greet}, how are you?")

def explain_features():
    speak("There are limited tasks I can do for now. Some are: ")
    speak("I can tell you the current time, date and day.")
    speak("I can search anything on google for you.")
    speak("I can check youtube for you.")
    speak("I can check your emails for you.")
    speak("I can play music for you.")
    speak("I can tell you the weather.")
    speak("I can help to remove your boredom by telling you jokes.")
    speak("I can motivate you by telling you quotes.")
    speak("I can help you to set reminders.")
    speak("I will let you know if you have any upcoming updates.")

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # This is a female voice
    engine.setProperty('rate', 145)  # Adjust the rate as needed
    engine.say(text)
    engine.runAndWait()

def try_again():
    try_again_audio = listen()
    try_again = recognizer.recognize_google(try_again_audio)
    if "yes" in try_again:
        return True
    else:
        speak("Okay")
        return False

def perform_search(query):
    query = query.replace("search", "")
    query = query.strip()
    if query:
        if "in browser" in query:
            query = query.replace("in browser", "")
            query = query.strip()
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
        else:
            try:
                response = openai.Completion.create(
                    engine="davinci",
                    prompt= query,
                    max_tokens=50,
                    n=1,
                    stop=None,
                )
                if response and 'choices' in response:
                    speak(response['choices'][0]['text'])
                    print(response['choices'][0]['text'])
                else:
                    speak("Sorry, I couldn't understand your search query.")
                    speak("Do you want me to try again?")
                    again = try_again()
                    if again:
                        perform_search(listen())

            except Exception as e:
                print('Your quota might have been exhausted. Please try again later.')
                speak("I think your quota might have been exhausted. Let me open in browser instead.")
                search_url = f"https://www.google.com/search?q={query}"
                webbrowser.open(search_url)
    else:
        speak("Sorry, I couldn't understand your search query.")
        speak("Do you want me to try again?")
        again = try_again()
        if again:
            perform_search(listen())

def open_apps():
    speak("What would you like to open?")
    app_query_audio = listen()
    app_query = recognizer.recognize_google(app_query_audio)
    app_query = app_query.lower()
    print(app_query)
    speak("Here you go.")
    if "notepad" in app_query:
        subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
    elif "calculator" in app_query:
        subprocess.Popen("C:\\Windows\\System32\\calc.exe")
    elif "paint" in app_query:
        subprocess.Popen("C:\\Windows\\System32\\mspaint.exe")
    elif "word" in app_query:
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    elif "powerpoint" in app_query:
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
    elif "spotify" in app_query:
        subprocess.Popen("C:\\Users\\ASUS\\AppData\\Roaming\\Spotify\\Spotify.exe")
    elif "vlc" in app_query:
        subprocess.Popen("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
    elif "code" in app_query:
        subprocess.Popen("C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif "browser" in app_query:
        subprocess.Popen("C:\\Users\\ASUS\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")
    elif "viber" in app_query:
        subprocess.Popen("C:\\Users\\ASUS\\AppData\\Local\\Viber\\Viber.exe")
    elif "no" in app_query:
        speak("Okay")
    else:
        speak(f"Sorry, I couldn't find any relevant results for '{app_query}'.")
        return open_apps()

def open_email():
    speak("Which mail? Personal or College?")
    print("Which mail? Personal or College?")
    mail_query_audio = listen()
    mail_query = recognizer.recognize_google(mail_query_audio)
    mail_query = mail_query.lower()
    print(mail_query)
    if "personal" in mail_query or "my" in mail_query or "mine" in mail_query or "myself" in mail_query or "me" in mail_query:
        speak("Opening Personal Gmail")
        webbrowser.open("") # Enter your personal gmail url here like https://mail.google.com/mail/u/0/#inbox
    elif "college" in mail_query:
        speak("Opening College Gmail")
        webbrowser.open("") # Enter your college gmail url here like https://mail.google.com/mail/u/1/#inbox
    elif "no" in mail_query or "close" in mail_query or "exit" in mail_query:
        speak("Okay")
    else:
        speak(f"Sorry, I couldn't find any relevant results for '{mail_query}'.")
        return open_email()

def sites_open():
    speak("Which site would you like to open?")
    speak("Up for movies or songs or youtube?")
    site_query_audio = listen()
    site_query = recognizer.recognize_google(site_query_audio)
    site_query = site_query.lower()
    if "movies" in site_query:
        speak("Opening Movies")
        url = "yts.mx"

        # Specify the browser executable path
        browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # Replace with the actual path to your browser executable

        # Open the URL in the specified browser
        subprocess.Popen([browser_path, url])

        # Wait for the browser window to close
        subprocess.call("pause", shell=True)
    elif "songs" in site_query or "song" in site_query or "music" in site_query:
        speak("Which song?")
        song_query_audio = listen()
        song_query = recognizer.recognize_google(song_query_audio)
        song_query = song_query.lower()
        if "no" in song_query or "close" in song_query or "exit" in song_query:
            speak("Okay")
            handle_command(listen())
        elif "" in song_query:
            speak("Sorry, I couldn't find any relevant results for '{song_query}'.")
            speak("Do you want me to try again?")
            again = try_again()
            if again == True:
                sites_open()
            else:
                speak("Okay")
        else:
            search_query = song_query + "song" # Append "music" to the search query
            youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(youtube_url)
    elif "youtube" in site_query:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "no" in site_query or "close" in site_query or "exit" in site_query:
        speak("Okay")

    else:
        speak(f"Sorry, I couldn't find any relevant results for '{site_query}'.")
        speak("Do you want me to try again?")
        again = try_again()
        if again == True:
            sites_open()
        else:
            speak("Okay")

def check_weather():
    speak("Weather of Kathmandu")
    city_name = "kathmandu"

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    api_key = "" # Enter your API key here

    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Specify the desired unit of measurement (metric, imperial, etc.)
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        main = weather_data["main"]
        temperature = main["temp"]
        feels_like = main["feels_like"]
        humidity = main["humidity"]
        wind = weather_data["wind"]
        wind_speed = wind["speed"]
        weather = weather_data["weather"]
        weather_description = weather[0]["description"]

        speak(f"The weather in {city_name} is {weather_description}. The temperature is {temperature} degrees Celsius, but it feels like {feels_like} degrees Celsius. The humidity is {humidity} percent and the wind speed is {wind_speed} kilometers per hour.")
    else:
        speak("Sorry, I couldn't find any relevant results for '{city_name}'.")
        speak("Do you want me to try again?")
        again = try_again()
        if again == True:
            check_weather()
        else:
            speak("Okay")

def play_games():
    game_query_audio = listen()
    game_query = recognizer.recognize_google(game_query_audio)
    game_query = game_query.lower()
    if 'yes' in game_query or "start" in game_query or "open" in game_query or "play" in game_query or "yeah" in game_query or "sure" in game_query:
        speak("Opening Valorant")
        subprocess.Popen("C:\\Riot Games\\Riot Client\\RiotClientServices.exe")
        game_mode()
    elif 'no' in game_query or "close" in game_query or "exit" in game_query:
        speak("Okay")
        handle_command(listen())
    else:
        speak(f"Sorry, I couldn't find any relevant results for '{game_query}'.")
        speak("Do you want me to try again?")
        again = try_again()
        if again == True:
            return play_games()
        else:
            speak("Okay")

    global game_mode_active
    game_mode_active = True

def check_unread_emails(username, password):
    try:
        # Connect to the Google IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)

        # Login to the Gmail account
        mail.login(username, password)

        # Select the mailbox to check (e.g., INBOX)
        mail.select("INBOX")

        # Search for unread emails
        _, data = mail.search(None, "UNSEEN")

        # Parse the result
        email_ids = data[0].split()
        num_unread_emails = len(email_ids)

        # Disconnect from the server
        mail.logout()
    
        return num_unread_emails

    except imaplib.IMAP4.error as e:
        print("An error occurred while connecting to the mail server:", e)
        return None

def speak_unread_emails():
    username1 = "" # Enter your email address here
    password1 = "" # Enter your app specific password here

    username2 = "" # Enter your email address here
    password2 = "" # Enter your app specific password here

    num_unread_emails1 = check_unread_emails(username1, password1)
    num_unread_emails2 = check_unread_emails(username2, password2)

    if num_unread_emails1 is None:
        speak("There is issue with the mail server. Internet connection may be offline.")
    else:
        if num_unread_emails1 == 0:
            speak("You have no unread emails in your personal account.")
        elif num_unread_emails1 == 1:
            speak("You have one unread email in your personal account.")
        else:
            speak(f"You have {num_unread_emails1} unread emails in your personal account.")
        speak("Do you want me to open personal mail?")
        open_mail = try_again()
        if open_mail == True:
            speak("Opening personal mail")
            webbrowser.open("") # Enter your personal email URL here
        else:
            speak("Okay")

    if num_unread_emails2 is None:
        speak("There is issue with the mail server. Internet connection may be offline.")
    else:
        if num_unread_emails2 == 0:
            speak("You have no unread emails in your college account.")
        elif num_unread_emails2 == 1:
            speak("You have one unread email in your college account.")
        else:
            speak(f"You have {num_unread_emails2} unread emails in your college account.")
        speak("Do you want me to open college mail?")
        open_mail = try_again()
        if open_mail == True:
            speak("Opening college mail")
            webbrowser.open("") # Enter your college email URL here
        else:
            speak("Okay")

def current_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def handle_note():
    speak("Do you want to read your notes or write a new one?")
    note_query_audio = listen()
    note_query = recognizer.recognize_google(note_query_audio)
    note_query = note_query.lower()
    if "read" in note_query:
        read_notes()
    elif "write" in note_query or "new" in note_query:
        take_note()
    elif "no" in note_query or "close" in note_query or "exit" in note_query:
        speak("Okay")
        handle_command(listen())
    else:
        speak(f"Sorry, I couldn't find any relevant results for '{note_query}'.")
        speak("Do you want me to try again?")
        again = try_again()
        if again == True:
            handle_note()
        else:
            speak("Okay")

def take_note():
    speak("What do you want to write down?")
    audio = listen()
    try:
        notes_query = recognizer.recognize_google(audio)
        notes_query = notes_query.lower()
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("You want to write this down?")
        speak(notes_query)

        note = {
            "date": current_date,
            "time": current_time,
            "note": notes_query
        }

        with open(os.path.join("Projects","Voice AI", "notes.json"), "r") as file:
            existing_notes = json.load(file)

        existing_notes.append(note)

        # Write all notes back to the file
        with open(os.path.join("notes.json"), "w") as file:
            json.dump(existing_notes, file, indent=4)

        speak("Note saved successfully.")

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        take_note()

def clear_notes():
    with open(os.path.join("notes.json"), "w") as file:
        json.dump([], file)

    speak("All notes have been removed.")

def read_notes():
    with open(os.path.join("notes.json"), "r") as file:
        notes = json.load(file)
        for note in notes:
            my_note = note["note"]
            date_note = note["date"]
            time = note["time"]
            speak(f"On {date_note} {time}, you wrote:")
            speak(my_note)

def remove_last_note():
    with open(os.path.join("notes.json"), "r") as file:
        notes = json.load(file)

    if len(notes) == 0:
        speak("There are no notes to remove.")
    else:
        removed_note = notes.pop()
        with open(os.path.join("notes.json"), "r") as file:
            json.dump(notes, file, indent=4)
            speak("The last note has been removed.")

        speak("The removed note was:")
        speak(removed_note["note"])

def say_joke():
    speak("Here is a joke for you")
    joke = pyjokes.get_joke()
    speak(joke)

'''def get_local_repo_name():
    # Change the current working directory to the repository directory
    repo_dir = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).strip().decode()
    os.chdir(repo_dir)

    # Get the repository name from the directory name
    repo_name = os.path.basename(repo_dir)

    return repo_name
def commit_in_github():
    # Create a GitHub instance using the access token
    g = Github(access_token)

    # Get the authenticated user
    
    # Get the repository name from the local repository
    repo_name = get_local_repo_name()

    # Get the repository object
    repo = g.get_repo(f"{repo_owner}/{repo_name}")

    # Rest of the code remains the same...

    # Prompt the user for the commit message
    commit_message = input("Enter the commit message: ")

    # Prompt the user for the file changes
    file_changes = input("Enter the file changes (separated by comma): ").split(",")

    # Create a list of file changes in the required format for the GitHub API
    changes = []
    for file_change in file_changes:
        change = {
            'path': file_change.strip(),
            'mode': '100644',  # Set the file mode (e.g., 100644 for regular files)
            'type': 'blob',  # Set the object type (e.g., 'blob' for file)
            'content': ''  # Leave empty if creating a new file, or provide the file content
        }
        changes.append(change)

    # Prompt the user for the parent commit (if applicable)
    parent_commit = input("Enter the SHA of the parent commit (leave empty for a new commit): ")

    # Create the commit using the GitHub API
    commit = repo.create_git_commit(commit_message, changes, parent_commit)

    # Push the commit to the repository
    ref = repo.get_git_ref("heads/master")  # Specify the reference for the branch you want to update
    ref.edit(commit.sha)

    print("Commit created and pushed successfully!")
'''

def handle_command(audio):
    try:
        print("Processing...")
        command = recognizer.recognize_google(audio)
        command = command.lower()

        if "introduce" in command or "Athena" in command or "who are you" in command:
            introduce()

        elif "hello" in command or "Hi" in command or "hai" in command:
            greeting()
        elif "open" in command or "launch" in command:
            open_apps()
        
        elif "athena" in command or "how are you" in command or "how are you doing" in command:
            speak(random.choice(greeting_quotes))
            speak(random.choice(howareyou_quotes))

        elif "meet " in command or "say hi to" in command:
            handle_greeting(command)

        elif "what can you do" in command or "what are your features" in command or "features of you" in command:
            explain_features()

        elif "what is my name" in command or "who am I" in command or "my name" in command:
            speak("Your name is Upson")

        elif "search" in command:
            if check_internet_connection():                
                speak("What would you like to search?")
                search_query_audio = listen()
                search_query = recognizer.recognize_google(search_query_audio)
                perform_search(search_query)
            else:
                speak("Sorry, I can't search without an internet connection.")

        elif "thank you" in command or "thanks" in command:
            welcome_quote = ["You're welcome", "No problem", "My pleasure", "It's my duty", "Glad to help", "Anytime"]
            random_welcome = random.choice(welcome_quote)
            speak(random_welcome)

        elif "remind me" in command or "set a reminder" in command or "create note" in command or "create a note" in command or "write a note" in command or "read note" in command or "read notes" in command or "my notes" in command or "make note" in command:
            handle_note()

        elif "remove last note" in command or "remove note" in command or "delete note" in command or "delete last note" in command or "clear all note" in command:
            if "last" in command:
                remove_last_note()
            elif "all" in command:
                clear_notes()
            else:
                speak("Sorry, I didn't catch that")
                handle_command(listen())

        elif "time" in command:
            current_time()
        
        elif "date" in command:
            today = date.today()
            current_date = today.strftime("%B %d, %Y")
            speak(f"The current date is {current_date}")
        
        elif "i am sleepy" in command or "bed" in command or "end up here" in command or "goodnight" in command or "Good night" in command or "good night" in command or "goodnight" in command:
            shutdown_pc()

        elif "check email" in command or "email" in command or "mail" in command:
            if check_internet_connection():
                open_email()
            else:
                speak("Sorry, I can't check your email without an internet connection.")

        elif "weather" in command or "temperature" in command or "climate" in command:
            if check_internet_connection():
                check_weather()
            else:
                speak("Sorry, I can't check the weather without an internet connection.")
                speak("I will inform you when the internet connection is back.")
                

        elif "bored" in command or "boring" in command or "youtube" in command or "movie" in command or "joke" in command or "jokes" in command:
            speak("I can help you with that.")
            speak("What would you like to do?")
            bored_query_audio = listen()
            bored_query = recognizer.recognize_google(bored_query_audio)
            bored_query = bored_query.lower()
            if "youtube" in bored_query or "site" in bored_query or "movie" in bored_query or "song" in bored_query or "music" in bored_query or "video" in bored_query:
                sites_open()
            elif "game" in bored_query or "play" in bored_query or "valorant" in bored_query or "valor" in bored_query:
                play_games()
            else:
                say_joke()

        elif "code help" in command or "chatgpt" in command or "Help" in command or "help" in command or "gpt" in command:
            speak("I called my friend GPT-3 to help you with your code.")
            webbrowser.open("https://chat.openai.com")

        elif "game" in command or "play game" in command:
            speak("What game would you like to play?")
            game_query_audio = listen()
            game_query = recognizer.recognize_google(game_query_audio)
            game_query = game_query.lower()
            if "valorant" in game_query or "valor" in game_query:
                speak("You only have Valorant installed. Do you want to play it?")
                play_games()
            elif "chess" in game_query or "latest" in game_query:
                speak("Opening chess.com")
                webbrowser.open("https://chess.com")
            else:
                speak("Sorry, but I don't have that game installed.")
                speak("I can only open Valorant and Chess.com for now.")


        elif "stop" in command or "see you" in command or "enough for today" in command:
            speak("Hibernating....")
            game_mode()
        
        elif "sleep" in command:
            speak("I will be running in the background. You can wake me up anytime.")
            speak(random.choice(bye_quotes))
            return False
        elif "check mouse" in command or "mouse app" in command or "mouse settings" in command:
            mouse_app()
        else:
            speak("Sorry, I couldn't get that. Can you please say it again?")

    except sr.UnknownValueError:
        print("Sorry, I am not able to do that. I am still in learning phase. So I am not good at it.")
        speak("Sorry, I am not able to do that. I am still in learning phase. So I am not good at it.")
        handle_command(listen())

    except sr.RequestError:
        print("Sorry, there was an issue with the service. Please try again later.")
        speak("Sorry, there was an issue with the service. Please try again later.")
        handle_command(listen())

    return True

def mouse_app():
    speak("Opening Mouse Controller")
    program_path = "C:\\Program Files (x86)\\FANTECH VX7 Gaming Mouse\\Gaming Mouse3.0.exe"

    command = [program_path]

    #open program as admin
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)


    # Wait for 10 seconds
    time.sleep(5)

    # Terminate the program
    process.terminate()

def shutdown_pc():
    speak("Do you want to shutdown your computer?")
    print("Shutdown query listening...")
    shutdown_query_audio = listen()
    shutdown_query = recognizer.recognize_google(shutdown_query_audio)
    shutdown_query = shutdown_query.lower()
    if 'yes' in shutdown_query or "yeah" in shutdown_query or "sure" in shutdown_query:
        speak("Shutting down the computer")
        speak("Before You go, I have a quote for you")
        speak(random.choice(good_night_quotes))
        os.system('shutdown /s /t 0')
    elif 'no' in shutdown_query or "nope" in shutdown_query:
        speak("Okay")
        handle_command(listen())
    else:
        speak(f"Sorry, I couldn't find any relevant results for '{shutdown_query}'.")
        speak("Do you want me to try again?")
        again = try_again()
        if again == True:
            return shutdown_pc()
        else:
            return handle_command(listen())

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise

        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)  # Set the timeout value as desired

        except sr.WaitTimeoutError:
            speak("Are you there?")
            return listen()

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please say it again?")
        return listen()

    except sr.RequestError:
        print("Sorry, there was an issue with the service. Please try again later.")
        return listen()

    return audio


def check_internet_connection():
    try:
        # Try to establish a connection to a reliable server
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def time_greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        quote = random.choice(good_morning_quotes)
        speak(quote)
        print(quote)
    elif hour >= 12 and hour < 18:
        quote = random.choice(good_afternoon_quotes)
        speak(quote)
        print(quote)
    else:
        quote = random.choice(good_evening_quotes)
        speak(quote)
        print(quote)

def game_mode():
    speak("Game mode activated")
    speak("I will be running in the background. You can wake me up anytime.")
    speak(random.choice(bye_quotes))
    while True:
        with sr.Microphone() as source:
            try:
                print("Listening...")
                wait_awake = recognizer.listen(source)
                wait_awake_text =   recognizer.recognize_google(wait_awake).lower()
                print(wait_awake_text)
                if "athena" in wait_awake_text or "help me" in wait_awake_text or "haseena" in wait_awake_text or "system online" in wait_awake_text or "system awake" in wait_awake_text:
                    time_greet()
                    speak(random.choice(awake_quotes))
                    while True:
                        audio_input = listen()
                        if not handle_command(audio_input):
                            break

                elif "stop" in wait_awake_text or "exit" in wait_awake_text:
                    speak("Goodbye!")
                    speak("Have a nice day! You can wake me up anytime.")
                    break

                else:
                    continue
                    
            except sr.UnknownValueError:
                continue

def main():
    time_greet()
    speak(random.choice(awake_quotes))
    if check_internet_connection():
        speak("While you were away, let me check if there is any important mail for you.")
        speak_unread_emails()
    else:
        speak("I see no internet connection. I will be running in offline mode.")
    while True:
        check_internet_connection()
        audio_input = listen()
        if not handle_command(audio_input):
            break
    root.mainloop()

# Run the program
if __name__ == "__main__":
    main()
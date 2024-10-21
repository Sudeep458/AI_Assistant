import pyttsx3 as p
import speech_recognition as sr
from YT_auto import Music  # Import the Music class from YT_auto.py
from News import News  # Import the News class from News.py
from weather import Weather  # Import the Weather class from weather.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import webbrowser  # Import webbrowser module

# Define the Inflow class for Wikipedia search
class Inflow:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_info(self, query):
        """Navigate to Wikipedia and search for the query."""
        self.driver.get("https://www.wikipedia.org")
        
        # Find the search input field and enter the query
        search_input = self.driver.find_element(By.NAME, "search")
        search_input.clear()  # Clear any existing text
        search_input.send_keys(query)

        # Submit the search form
        search_input.submit()

        # Wait for the page to load (you can use WebDriverWait for better practice)
        time.sleep(3)  # Adjust time as needed

        # Get the title of the page as an example of information retrieval
        page_title = self.driver.title
        print(f"Page Title: {page_title}")

    def close_driver(self):
        """Close the browser."""
        self.driver.quit()

# Text-to-Speech Initialization
engine = p.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

# Speech Recognition Initialization
r = sr.Recognizer()

# Greet user and listen for input
speak("Hello sir, I'm your voice assistant. How are you?")
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")

    if "what" in text and "about" in text and "you" in text:
        speak("I am also having a good day, sir.")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

speak("What can I do for you?")

# Listen for another command
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")

    if "information" in text:
        speak("You need information on which topic?")
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)

        try:
            infor = r.recognize_google(audio)
            print(f"You asked about: {infor}")

            # Instantiate Inflow and get information
            assist = Inflow()
            assist.get_info(infor)

            input("Press Enter to close the browser...")  # Wait for user input before closing

            assist.close_driver()

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    elif "play" in text or "video" in text:  # Check if user wants to play a video
        speak("What video do you want to play?")
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)

            try:
                vid = r.recognize_google(audio)
                print(f"Playing {vid} on YouTube.")
                
                music_assist = Music()  # Instantiate Music class
                music_assist.play(vid)

                input("Press Enter to close the browser...")  # Wait for user input before closing

                music_assist.close_driver()
                
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

    elif "top news" in text:  # Check if user wants top news
        speak("Fetching top news for you.")
        
        news_assist = News()  # Instantiate News class
        articles = news_assist.get_top_news()
        
        # Create HTML file with news articles
        news_assist.create_news_html(articles)

        # Open the generated HTML file in a new Chrome tab
        webbrowser.open_new_tab('top_news.html')

    elif "weather" in text:  # Check if user wants weather information
        speak("Which city's weather do you want to know?")
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)

            try:
                city = r.recognize_google(audio)
                print(f"Fetching weather for {city}.")

                weather_assist = Weather()  # Instantiate Weather class
                weather_data = weather_assist.get_weather(city)
                
                # Create HTML file with weather information
                weather_assist.create_weather_html(weather_data)

                # Open the generated HTML file in a new Chrome tab using full path
                webbrowser.open_new_tab('D:\\Ai-Assistant-main\\weather_info.html')

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
    
''' BASIC VOICE ASSISTANT '''


import speech_recognition as sr
from datetime import datetime
import webbrowser
import pyttsx3

print("Welcome World of Jarvis")

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

while True:
  with sr.Microphone() as source:
      print("Listening...")
      recognizer.adjust_for_ambient_noise(source)
      audio = recognizer.listen(source)
    
  try:
      command = recognizer.recognize_google(audio).lower()
      print(f"You said: {command}")
        
      if "hello" in command:
        speak("Hello! How can I help you today?")
    
        
      elif "date" in command:
        current_date = datetime.today().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
            
             
      elif "time" in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
        
      elif "search " in command:
        search_query = command.replace("search for", "").strip()
        if search_query:
             speak(f"Searching for {search_query} ")
             webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
             speak("I didn't hear a search query.")
        
      elif "quite" in command or "exit" in command:
        speak("Goodbye!")
        break
        
      else:
        speak("Sorry, I don't know how to help with that.")
    
  except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
    
  except sr.RequestError:
        speak("Sorry, my speech service is down.")

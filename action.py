
# import datetime
# import speak
# import webbrowser
# import weather
# import os
# import requests


# def google_search(query, api_key, cx):
#     """
#     Perform a Google Custom Search using the API key and Search Engine ID (cx).
#     """
#     url = f"https://www.googleapis.com/customsearch/v1"
#     params = {
#         "q": query,
#         "key": api_key,
#         "cx": cx,
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         results = response.json().get("items", [])
#         if results:
#             return results[0].get("link", "No link found")
#         else:
#             return "No results found"
#     else:
#         return f"Error: {response.status_code}"


# def Action(send):   
#     data_btn = send.lower()
#     api_key = "AIzaSyDu6mOUlFQqViUbremiNtVYrLRszwnn52A"  # Your Google API Key
#     search_engine_id = "60d9e418be05a4c65"  # Replace with your Search Engine ID

#     if "what is your name" in data_btn:
#         speak.speak("My name is NOVA")  
#         return "My name is NOVA"

#     elif "hello" in data_btn or "hye" in data_btn or "hay" in data_btn: 
#         speak.speak("Hey Om, how can I help you!")  
#         return "Hey Om, how can I help you!"

#     elif "how are you" in data_btn:
#         speak.speak("I am doing great these days, Om") 
#         return "I am doing great these days, Om"   

#     elif "thank you" in data_btn or "thank" in data_btn:
#         speak.speak("It's my pleasure, Om, to stay with you")
#         return "It's my pleasure, Om, to stay with you"      

#     elif "good morning" in data_btn:
#         speak.speak("Good morning, Om. I think you might need some help.")
#         return "Good morning, Om. I think you might need some help."   

#     elif "time" in data_btn:
#         current_time = datetime.datetime.now()
#         time = f"{current_time.hour} Hour : {current_time.minute} Minute"
#         speak.speak(time)
#         return time 

#     elif "shutdown" in data_btn or "quit" in data_btn:
#         speak.speak("Ok, sir")
#         return "Ok, sir"  

#     elif "play music" in data_btn or "song" in data_btn:
#         webbrowser.open("https://gaana.com/")   
#         speak.speak("Gaana.com is now ready for you. Enjoy your music.")                   
#         return "Gaana.com is now ready for you. Enjoy your music."

#     elif "open google" in data_btn or "google" in data_btn:
#         url = 'https://google.com/'
#         webbrowser.get().open(url)
#         speak.speak("Google open")  
#         return "Google open"

#     elif "youtube" in data_btn or "open youtube" in data_btn:
#         url = 'https://youtube.com/'
#         webbrowser.get().open(url)
#         speak.speak("YouTube open") 
#         return "YouTube open"

#     elif "weather" in data_btn:
#         ans = weather.Weather()
#         speak.speak(ans) 
#         return ans

#     elif "music from my laptop" in data_btn:
#         url = 'D:\\music' 
#         songs = os.listdir(url)
#         os.startfile(os.path.join(url, songs[0]))
#         speak.speak("Songs playing...")
#         return "Songs playing..." 

#     elif "open upes" in data_btn or "upes" in data_btn:
#         url = "https://www.upes.ac.in/"
#         webbrowser.get().open(url)
#         speak.speak("UPES website is now open.")
#         return "UPES website is now open."

#     elif "search" in data_btn:
#         # Extract search query after "search"
#         query = data_btn.replace("search", "").strip()
#         if query:
#             result = google_search(query, api_key, search_engine_id)
#             speak.speak(f"Here is what I found: {result}")
#             return f"Here is what I found: {result}"
#         else:
#             speak.speak("Please provide something to search for.")
#             return "Please provide something to search for."

#     else:
#         speak.speak("I'm unable to understand!")
#         return "I'm unable to understand!"






# import datetime
# import speak
# import webbrowser
# import weather
# import os


# def Action(send):   
#     data_btn = send.lower()

#     if "what is your name" in data_btn:
#         speak.speak("My name is NOVA")  
#         return "My name is NOVA"

#     elif "hello" in data_btn or "hye" in data_btn or "hay" in data_btn: 
#         speak.speak("Hey Om, how can I help you!")  
#         return "Hey Om, how can I help you!"

#     elif "how are you" in data_btn:
#         speak.speak("I am doing great these days, Om") 
#         return "I am doing great these days, Om"   

#     elif "thank you" in data_btn or "thank" in data_btn:
#         speak.speak("It's my pleasure, Om, to stay with you")
#         return "It's my pleasure, Om, to stay with you"      

#     elif "good morning" in data_btn:
#         speak.speak("Good morning, Om. I think you might need some help.")
#         return "Good morning, Om. I think you might need some help."   

#     elif "time" in data_btn:
#         current_time = datetime.datetime.now()
#         time = f"{current_time.hour} Hour : {current_time.minute} Minute"
#         speak.speak(time)
#         return time 

#     elif "shutdown" in data_btn or "quit" in data_btn:
#         speak.speak("Ok, sir")
#         return "Ok, sir"  

#     elif "play music" in data_btn or "song" in data_btn:
#         webbrowser.open("https://gaana.com/")   
#         speak.speak("Gaana.com is now ready for you. Enjoy your music.")                   
#         return "Gaana.com is now ready for you. Enjoy your music."

#     elif "open google" in data_btn or "google" in data_btn:
#         url = 'https://google.com/'
#         webbrowser.get().open(url)
#         speak.speak("Google open")  
#         return "Google open"

#     elif "youtube" in data_btn or "open youtube" in data_btn:
#         url = 'https://youtube.com/'
#         webbrowser.get().open(url)
#         speak.speak("YouTube open") 
#         return "YouTube open"

#     elif "weather" in data_btn:
#         ans = weather.Weather()
#         speak.speak(ans) 
#         return ans

#     elif "music from my laptop" in data_btn:
#         url = 'D:\\music' 
#         songs = os.listdir(url)
#         os.startfile(os.path.join(url, songs[0]))
#         speak.speak("Songs playing...")
#         return "Songs playing..." 

#     elif "open upes" in data_btn or "upes" in data_btn:
#         url = "https://www.upes.ac.in/"
#         webbrowser.get().open(url)
#         speak.speak("UPES website is now open.")
#         return "UPES website is now open."

#     elif "open campus video" in data_btn or "campus video" in data_btn:
#         url = "https://www.youtube.com/watch?v=hZvkVDX2GYw"
#         webbrowser.get().open(url)
#         speak.speak("Campus video is now playing.")
#         return "Campus video is now playing."
    
#     elif "open Anish" in data_btn or "Anish" in data_btn:
#         url = "https://www.upes.ac.in/faculty/school-of-computer-science/dr-anish-kumar-vishwakarma"
#         webbrowser.get().open(url)
#         speak.speak("Professor Dr. Anish Kumar Vishwakarma's profile is now open.")
#         return "Professor Dr. Anish Kumar Vishwakarma's profile is now open."

#     elif "open vijendra" in data_btn or "vijendra" in data_btn:
#         url = "https://www.upes.ac.in/faculty/school-of-computer-science/vijendra-singh"
#         webbrowser.get().open(url)
#         speak.speak("Professor Vijendra Singh's profile is now open.")
#         return "Professor Vijendra Singh's profile is now open."

#     else:
#         speak.speak("I'm unable to understand!")
#         return "I'm unable to understand!"






import datetime
import speak
import webbrowser
import weather
import os
import requests


def google_search(query, api_key, cx):
    """
    Perform a Google Custom Search using the API key and Search Engine ID (cx).
    """
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cx,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("items", [])
        if results:
            # Return the snippet (direct answer) and link of the first result
            snippet = results[0].get("snippet", "No snippet available")
            link = results[0].get("link", "No link found")
            return snippet, link
        else:
            return "No results found", None
    else:
        return f"Error: {response.status_code}", None


def Action(send):   
    data_btn = send.lower()
    api_key = "AIzaSyDu6mOUlFQqViUbremiNtVYrLRszwnn52A"  # Your Google API Key
    search_engine_id = "60d9e418be05a4c65"  # Replace with your Search Engine ID

    if "search" in data_btn:
        # Extract search query after "search"
        query = data_btn.replace("search", "").strip()
        if query:
            snippet, link = google_search(query, api_key, search_engine_id)
            if link:
                # Speak out the snippet
                speak.speak(f"Here is what I found: {snippet}. Opening the link for you.")
                # Automatically open the first link in the browser
                webbrowser.open(link)
                return f"Here is what I found: {snippet}. Opening the link: {link}"
            else:
                speak.speak(snippet)  # Handle errors or "No results found"
                return snippet
        else:
            speak.speak("Please provide something to search for.")
            return "Please provide something to search for."

    elif "what is your name" in data_btn:
        speak.speak("My name is NOVA")  
        return "My name is NOVA"

    elif "hello" in data_btn or "hye" in data_btn or "hay" in data_btn: 
        speak.speak("Hey Om, how can I help you!")  
        return "Hey Om, how can I help you!"

    elif "how are you" in data_btn:
        speak.speak("I am doing great these days, Om") 
        return "I am doing great these days, Om"   

    elif "thank you" in data_btn or "thank" in data_btn:
        speak.speak("It's my pleasure, Om, to stay with you")
        return "It's my pleasure, Om, to stay with you"      

    elif "good morning" in data_btn:
        speak.speak("Good morning, Om. I think you might need some help.")
        return "Good morning, Om. I think you might need some help."   

    elif "time" in data_btn:
        current_time = datetime.datetime.now()
        time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        speak.speak(time)
        return time 

    elif "shutdown" in data_btn or "quit" in data_btn:
        speak.speak("Ok, sir")
        return "Ok, sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("Gaana.com is now ready for you. Enjoy your music.")                   
        return "Gaana.com is now ready for you. Enjoy your music."

    elif "open google" in data_btn or "google" in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("Google open")  
        return "Google open"

    elif "youtube" in data_btn or "open youtube" in data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"

    elif "weather" in data_btn:
        ans = weather.Weather()
        speak.speak(ans) 
        return ans

    elif "music from my laptop" in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("Songs playing...")
        return "Songs playing..." 

    elif "open upes" in data_btn or "upes" in data_btn:
        url = "https://www.upes.ac.in/"
        webbrowser.get().open(url)
        speak.speak("UPES website is now open.")
        return "UPES website is now open."

    elif "open campus video" in data_btn or "campus video" in data_btn:
        url = "https://www.youtube.com/watch?v=hZvkVDX2GYw"
        webbrowser.get().open(url)
        speak.speak("Campus video is now playing.")
        return "Campus video is now playing."
    
    elif "open Anish" in data_btn or "Anish" in data_btn:
        url = "https://www.upes.ac.in/faculty/school-of-computer-science/dr-anish-kumar-vishwakarma"
        webbrowser.get().open(url)
        speak.speak("Professor Dr. Anish Kumar Vishwakarma's profile is now open.")
        return "Professor Dr. Anish Kumar Vishwakarma's profile is now open."

    elif "open vijendra" in data_btn or "vijendra" in data_btn:
        url = "https://www.upes.ac.in/faculty/school-of-computer-science/vijendra-singh"
        webbrowser.get().open(url)
        speak.speak("Professor Vijendra Singh's profile is now open.")
        return "Professor Vijendra Singh's profile is now open."

    else:
        speak.speak("I'm unable to understand!")
        return "I'm unable to understand!"

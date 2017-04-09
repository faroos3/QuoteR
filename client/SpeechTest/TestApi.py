# Tests speech api
import speech_recognition as sr
from oauth2client.client import GoogleCredentials
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
     #right now , we are using the default API key
    #`r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")` will get a different one
     #instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
   print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


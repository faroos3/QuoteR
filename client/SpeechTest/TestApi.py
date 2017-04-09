# Tests speech api
import speech_recognition as sr
from oauth2client.client import GoogleCredentials
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# This is an alternative to goolge if we want, but it's also a requirment for the google api
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

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




#  Google Cloud Speech - this requires a service account, we dont have one right now
#GOOGLE_CLOUD_SPEECH_CREDENTIALS = GoogleCredentials.get_application_default()
#try:
  #  print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
#except sr.UnknownValueError:
 #   print("Google Cloud Speech could not understand audio")
#except sr.RequestError as e:
    #print("Could not request results from Google Cloud Speech service; {0}".format(e))

from ibm_watson import TextToSpeechV1  # type: ignore
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator  # type: ignore
from dotenv import load_dotenv
from os import getenv

load_dotenv()
apikey = getenv("API_KEY")
url = getenv("LINK")

authenticator = IAMAuthenticator(apikey)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(url)

with open('first.wav','wb') as audio_file:
    audio_file.write(text_to_speech.synthesize('hello world this is the king',voice='en-US_HenryV3Voice',accept='audio/mp3').get_result().content)

from playsound import playsound

playsound('first.wav')
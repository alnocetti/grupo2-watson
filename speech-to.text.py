import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('e6BZxl90o8UFcTKnaYRb-_4E4H_bWEImpOaAq3gxzX3O')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/6a8ceb8f-87f4-406f-a8ad-4839b95f614c')

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

myRecognizeCallback = MyRecognizeCallback()

__file__ = '/home/alnocetti/Grabaciones/'
with open(join(dirname(__file__), 'Test'),
              'rb') as audio_file:
    audio_source = AudioSource(audio_file)
    speech_to_text.recognize_using_websocket(
        audio=audio_source,
        content_type='audio/ogg;codecs=vorbis',
        recognize_callback=myRecognizeCallback,
        model='es-AR_BroadbandModel',
        keywords=['hola', 'nombre'],
        keywords_threshold=0.5,
        max_alternatives=3)

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']



authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-01-13',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

def englishToFrench(myText1):
    """
    english to text translation
    """
    myFrenchtranslator = language_translator.translate(
        text=myText1,
        model_id="en-fr"
    ).get_result()

    return myFrenchtranslator.get("translations")[0].get("translation")



def frenchToEnglish(myText2):
    """
    french to english translation
    """
    myEnglishtranslator = language_translator.translate(
        text=myText2,
        model_id="fr-en"
    ).get_result()

    return myEnglishtranslator.get("translations")[0].get("translation")



""" 
print(englishToFrench('Good morning'))

print(frenchToEnglish('Bonjour, bonjour'))
"""
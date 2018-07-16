'''
# 1.install library
# $ pip install google-cloud-translate
'''
import io
import os
from google.cloud import translate

# Set google application credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./credential/vision-api-exit-89121177417b.json"

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = u"Print graph paper free from your computer. This site is perfect for science and math homework, craft projects and other graph paper needs. All graph paper files are optimized PDF documents requiring Adobe Reader for viewing."
# The target language
target = 'ko'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))
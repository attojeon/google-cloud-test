'''
# Label(대표어휘, 표상어휘) 검출하기
# 1. install library
# $ pip install google-cloud-vision
'''
import io
import os
import google.cloud.vision

# Set google application credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./credential/vision-api-exit-89121177417b.json"

# Create a Vision client.
vision_client = google.cloud.vision.ImageAnnotatorClient()

# TODO (Developer): Replace this with the name of the local image
# file to analyze.
image_file_name = './images/sportscar.jpg'
with io.open(image_file_name, 'rb') as image_file:
    content = image_file.read()

# Use Vision to label the image based on content.
image = google.cloud.vision.types.Image(content=content)
response = vision_client.label_detection(image=image)
print(response)
print('='*88)
print('Labels:')
for label in response.label_annotations:
    print('라벨이름:', label.description, '\t\t\t확률:', label.score)

'''
response = vision_client.text_detection(image=image)
print('='*88)
print(response.text_annotations)
'''

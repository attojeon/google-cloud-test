'''
# Text 검출하기 + Text 위치 사각형 표시하기
# 1. install library
# $ pip install google-cloud-vision
'''
import io
import os
import google.cloud.vision
from PIL import Image, ImageDraw 

# Set google application credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./credential/vision-api-exit-89121177417b.json"

# Create a Vision client.
vision_client = google.cloud.vision.ImageAnnotatorClient()

# TODO (Developer): Replace this with the name of the local image
# file to analyze.
image_file_name = './images/president.jpg'
with io.open(image_file_name, 'rb') as image_file:
    content = image_file.read()

# Use Vision to label the image based on content.
image = google.cloud.vision.types.Image(content=content)
response = vision_client.text_detection(image=image)
print('Response:')
print(response)
print('='*88)
print('Texts:')
print('='*88)
texts = response.text_annotations

# 새로운 이미지 파일에 바운딩박스 그리기
bounds = []
for text in texts:
    #print('{}'.format(text.description))
    bounds.append(text.bounding_poly)
    print('-'*44)

image = Image.open(image_file_name)
draw = ImageDraw.Draw(image)
print(bounds)
for bound in bounds:
    draw.polygon([
        bound.vertices[0].x, bound.vertices[0].y,
        bound.vertices[1].x, bound.vertices[1].y,
        bound.vertices[2].x, bound.vertices[2].y,
        bound.vertices[3].x, bound.vertices[3].y], None, 'red')

image.save('./images/pre.jpg')
image.show()

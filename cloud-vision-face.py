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
image_file_name = './images/peoples.jpg'
with io.open(image_file_name, 'rb') as image_file:
    content = image_file.read()

# Use Vision to label the image based on content.
image = google.cloud.vision.types.Image(content=content)
# End migration_image_file

response = vision_client.face_detection(image=image)
print('Response:')
print(response)
print('='*88)
print('Faces:')
print('='*88)
faces = response.face_annotations

likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')
print('Faces:')

for face in faces:
    print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
    print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
    print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in face.bounding_poly.vertices])

    print('face bounds: {}'.format(','.join(vertices)))


# 새로운 이미지 파일에 바운딩박스 그리기
bounds = []
for face in faces:
    #print('{}'.format(text.description))
    bounds.append(face.fd_bounding_poly)
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

image.save('./images/fd_after.jpg')
image.show()
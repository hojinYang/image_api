import os
import random
from flask import Flask, send_file

app = Flask(__name__)
IMAGE_DIR = "images"

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/sample')
def sample():
    images = os.listdir(IMAGE_DIR)
    print(images)
    image_files = [img for img in images]
    selected_image = random.choice(image_files)
    #return send_file(os.path.join(IMAGE_DIR, selected_image), mimetype='image/jpg')
    return send_file( "images/"+selected_image, mimetype='image/jpg')
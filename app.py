import sys
import os

# Set default encoding to UTF-8
os.environ["PYTHONIOENCODING"] = "UTF-8"

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np 

# Initialize the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load the trained model
model = load_model('plant_disease_model.h5')

# Define the labels
labels = ['Healthy', 'Powdery', 'Rust']

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            # Save the uploaded file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            
            # Preprocess the image
            img = image.load_img(file_path, target_size=(225, 225))
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            img /= 255.0
            
            # Make a prediction
            predictions = model.predict(img)
            predicted_class = labels[np.argmax(predictions)]
            
            return render_template('result.html', prediction=predicted_class, img_path=file_path)
    except UnicodeEncodeError as e:
        print(f"UnicodeEncodeError: {e}")
        return "An encoding error occurred. Please try again."

# Serve the uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except UnicodeEncodeError as e:
        print(f"UnicodeEncodeError while serving file: {e}")
        return "An encoding error occurred while serving the file. Please try again."

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)

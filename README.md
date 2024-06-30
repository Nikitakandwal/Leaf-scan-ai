# Leaf Scan AI

Leaf Scan AI is a web application for plant disease recognition using deep learning. It allows users to upload images of plant leaves to get instant predictions about possible diseases affecting the plants.

## Features

- **Upload Image:** Users can upload an image of a plant leaf.
- **AI Prediction:** Utilizes a Convolutional Neural Network (CNN) model to predict plant diseases based on uploaded images.
- **User-Friendly Interface:** Simple and intuitive web interface for easy interaction.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Machine Learning:** TensorFlow, Keras
- **Deployment:** Deployed locally


## Folder Structure
```bash
leaf-scan-ai/
├── app.py            # Flask application file
├── templates/        # HTML templates
│   └── index.html    # Main HTML file for the application
├── static/           # Static files (CSS, images)
│   ├── styles.css    # CSS styles for the application
│   └── favicon.png   # Favicon image
├── model.h5          # Trained CNN model (example)
└── README.md         # This file, providing project information
```

This project does not include the pre-trained model file (`plant_disease_model.h5`). To use the plant disease recognition feature, you will need to train your own model using the dataset.

## Demo Video

Watch a quick demo of the Leaf Scan AI in action:

https://github.com/Nikitakandwal/Leaf-scan-ai/assets/98966392/a187ca40-61c5-48db-aaa1-f6da0b801167

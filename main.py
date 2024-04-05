import os
import json
from PIL import Image

import numpy as np
import tensorflow as tf
import streamlit as st

working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/trained_model/pathogen_prediction_model.h5"
# Load the pre-trained model
model = tf.keras.models.load_model(model_path)

# loading the class names
class_indices = json.load(open(f"{working_dir}/class_indices.json"))

# Function to Load and Preprocess the Image using Pillow
def load_and_preprocess_image(image_path, target_size=(224, 224)):
    # Load the image
    img = Image.open(image_path)
    # Resize the image
    img = img.resize(target_size)
    # Convert the image to a numpy array
    img_array = np.array(img)
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    # Scale the image values to [0, 1]
    img_array = img_array.astype('float32') / 255.
    return img_array


# Function to Predict the Class of an Image
def predict_image_class(model, image_array, class_indices):
    predictions = model.predict(image_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]
    return predicted_class_name


pathogen_solutions = {
    'bacteria': 'Apply a bactericide containing copper compounds.',
    'fungi': 'Use a fungicide targeted to the specific fungal species causing the infection.',
    'pests': 'Implement integrated pest management practices, including cultural and biological controls, and consider using targeted pesticides as a last resort.',
    'virus': 'Practice strict sanitation measures, including the removal and destruction of infected plants, and implement vector control strategies where applicable.',
    'healthy': 'No treatment needed. Continue to monitor the plant for signs of disease or pest infestation.'
}


pathogen_explanations = {
    'bacteria': 'Bacterial infections in plants can be controlled by applying a copper-based fungicide, which acts as a bactericide. This helps prevent the spread of bacteria and promotes plant health.',
    'fungi': 'Fungal infections in plants require the use of fungicides that are effective against the specific type of fungus causing the infection. Using a broad-spectrum fungicide may not provide adequate control.',
    'pests': 'Pest infestations in plants can be managed by using pesticides targeted at the specific pests identified. Different pests may require different pesticides, so it\'s essential to identify the pest accurately before treatment.',
    'virus': 'Viral infections in plants cannot be treated with fungicides or pesticides. The best way to prevent the spread of viral diseases is to remove and destroy infected plants promptly. This helps prevent the virus from spreading to healthy plants.',
    'healthy': 'The plant appears to be healthy and does not require any treatment at this time. Continue to monitor the plant for signs of disease or pest infestation.'
}

pathogen_learn_more_links = {
    'bacteria': 'https://ohioline.osu.edu/factsheet/plpath-gen-6',
    'fungi': 'https://www.gardentech.com/blog/pest-id-and-prevention/prevent-and-control-fungal-disease-in-fruit-and-vegetable-gardens',
    'pests': 'https://hicare.in/blog/how-to-keep-pests-away-from-the-garden/',
    'virus': 'https://www.lovethegarden.com/uk-en/article/virus',
    'healthy': 'https://www.fnp.com/article/how-to-keep-your-plants-healthy-and-disease-free',
}



# Streamlit App
st.title('Pathogen Classifier')

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1:
        resized_img = image.resize((224, 224))
        st.image(resized_img)

    with col2:
        if st.button('Classify'):
            # Preprocess the uploaded image and predict the class
            preprocessed_img = load_and_preprocess_image(uploaded_image)
            prediction = predict_image_class(model, preprocessed_img, class_indices)
            solution = pathogen_solutions.get(prediction.lower(), 'Solution not available')
            explanations = pathogen_explanations.get(prediction.lower(), 'Explanation not available')
            st.success(f'Prediction: {prediction.capitalize()}')
            st.info(f'Solution: {solution}')
            st.info(f'Explanation: {explanations}')

            if prediction.lower() in pathogen_learn_more_links:
                if prediction.lower() == 'healthy':
                    learn_more_text = 'Learn more about how to keep plants healthy'
                else:
                    learn_more_text = f'Learn More about {prediction.capitalize()} Prevention'
                learn_more_link = pathogen_learn_more_links[prediction.lower()]
                st.markdown(f"[{learn_more_text}]({learn_more_link})")
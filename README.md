# Universal Pathogen Detection In Plants Using Deep Learning Techniques


## Overview
PathoPlant aims to develop a deep learning-based solution for the early detection and identification of pathogens in plant species. By leveraging state-of-the-art deep learning models, the project seeks to address the challenges associated with manual plant pathogen diagnosis and monitoring, thereby improving agricultural productivity and crop yield.

## Key Features
- **Advanced Deep Learning Model:** Incorporates a state-of-the-art convolutional neural network (CNN), ResNet50 architecture, for accurate identification of various plant pathogens.
- **Multi-Class Pathogen Detection:** Develop a model capable of detecting multiple classes of plant pathogens, including bacteria, fungi, pests, viruses and also healthy plants.
- **Diverse and Comprehensive Dataset:** Utilizes a diverse dataset sourced from multiple repositories, ensuring thorough training and validation across different types of pathogens and plant species.
- **Robust Image Preprocessing Techniques:** Employs advanced preprocessing techniques such as resizing, data augmentation, and normalization to standardize and enhance the quality of input images, improving model performance.
- **Comprehensive Evaluation Metrics:** Evaluates model performance using metrics like accuracy, precision, recall, and F1-score, along with visualization tools like confusion matrices, providing detailed insights into classification capabilities.
- **Real-world Generalization Testing:** Undergoes rigorous testing with an independent dataset to assess generalization and robustness, ensuring effective deployment in practical agricultural settings.

  ## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kanishk3813/PlantPath.git
- Download the dataset from [Kaggle](https://www.kaggle.com/datasets/kanishk3813/pathogen-dataset) or curate your own dataset.
- Please Note : Install necessary python libraries by (`pip install {library_name}`) .

  ## Usage

1. **Training the Model:** Train the deep learning model using the provided dataset, adjusting hyperparameters as necessary to optimize performance.
2. **Model Evaluation:** Evaluate the performance of the trained model using appropriate metrics and validation techniques to ensure accuracy and reliability.
3. **Saving the Model:** Save the trained model as a .h5 file for future use and deployment in production environments.
4. **Configuration Setup:** Configure the necessary path folders in the main.py file to ensure seamless integration with your local environment.
5. **Running the Application:** Execute the application by running **'streamlit run main.py'**, allowing users to interact with the system and benefit from its capabilities.
   **Note:** The mobile application of the project is under development.

## Contributing

Contributions are welcome! If you'd like to contribute to PathoPlant, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to your forked repository (`git push origin feature/your-feature-name`).
5. Create a pull request detailing your changes and their purpose.

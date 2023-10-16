# Soybean Leaf Classification using EfficientNet

## Project Overview

This repository contains the code and resources for a Deep Learning project focused on classifying soybean leaves into healthy or diseased categories using Convolutional Neural Networks (CNNs). The project achieved an impressive test set accuracy of 93% by leveraging the state-of-the-art EfficientNet model architecture. The dataset used for training and evaluation is the "SoyNet" dataset, which consists of images of Indian soybean leaves.

## Dataset

### SoyNet Dataset

The SoyNet dataset contains a diverse collection of soybean leaf images, including healthy and diseased leaves. This dataset was specifically curated for this project and is designed to address the classification task of distinguishing between healthy and diseased soybean leaves. The dataset is divided into training, validation, and test sets to facilitate model training and evaluation.

Please note that this dataset is not publicly available in this repository, and you will need to obtain it separately for use in this project. Ensure that the dataset is structured with appropriate directories for each class, i.e., "healthy" and "diseased."

## Model Architecture

### EfficientNet

EfficientNet is a family of convolutional neural network architectures that are known for their excellent performance and efficiency. These models have been widely used for various computer vision tasks due to their ability to achieve high accuracy with relatively fewer parameters compared to traditional CNN architectures. In this project, the EfficientNet model was utilized as the backbone for soybean leaf classification.

## Code Structure

The project's code is organized into the following directories:

- **requirements.txt** file that highlights all necessary dependencies
- **.ipynb file**

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/soybean-leaf-classification.git
   cd soybean-leaf-classification
   ```

2. Obtain the SoyNet dataset and structure it as described in the "Dataset" section. Place it in the `data` directory.

3. Install the required Python libraries and dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Train the model using the provided Jupyter notebooks in the `notebooks` directory. Start with data preprocessing, model training, and evaluation.

5. After training, the model checkpoints and evaluation results will be saved in the `results` directory.

## Results

The project achieved a test set accuracy of 93%, demonstrating the effectiveness of the EfficientNet model for soybean leaf classification. Detailed evaluation metrics, including confusion matrices and classification reports, can be found in the project's notebooks and results directory.

## Conclusion

This project showcases the application of deep learning techniques, specifically the EfficientNet model, for the classification of soybean leaves as healthy or diseased. The high accuracy achieved suggests the potential for utilizing similar approaches to assist in real-world agricultural tasks, such as crop disease detection and monitoring.

Feel free to explore the code and adapt it to your specific needs or dataset. If you have any questions or need further assistance, please don't hesitate to reach out to the project contributors.

Happy coding and best of luck with your soybean leaf classification project!

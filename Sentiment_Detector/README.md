# Sentiment Detection

This project implements a sentiment detection model that analyzes the sentiment of text data, classifying it as positive, negative, or neutral. The model is trained on a dataset of labeled movie reviews.

## Dataset

The sentiment detection model is trained on the IMDb movie reviews dataset. The dataset consists of movie reviews along with their corresponding sentiment labels (positive or negative). The dataset is stored in the file `imdb_dataset.csv`. Please make sure to place the dataset file in the same directory as the code.

## Dependencies

- Python 3.x
- pandas
- scikit-learn

Install the required dependencies using the following command:


## Usage

1. Clone this repository or download the code files.
2. Place the `imdb_dataset.csv` file in the same directory as the code.
3. Run the `sentiment_detection.py` script.


4. The model will be trained on the dataset and will perform sentiment detection on new text data.
5. The accuracy of the model will be displayed, and you can also test the model on new reviews by modifying the `new_reviews` list in the code.

## Results

The sentiment detection model achieves an accuracy of approximately 85% on the test set. The model can effectively classify text data into positive, negative, or neutral sentiment categories.

## Future Improvements

- Explore different feature extraction techniques like TF-IDF or word embeddings to enhance the model's performance.
- Experiment with different machine learning algorithms such as Naive Bayes, Support Vector Machines, or neural networks.
- Increase the size of the training dataset to improve the model's generalization ability.
- Implement a web interface or API for easy interaction with the sentiment detection model.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

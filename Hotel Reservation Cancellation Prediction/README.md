# Hotel Booking Cancellation Prediction Model

Model takes in factors such as lead times, type of room reserved, average cost of rooms booked amongst other factors to determine if guest is going to cancel the booking or not. Model trained using [Hotel Reservations Dataset](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset). Final model utilizes XGBoost and hyperparameter tuning was done using Optuna. Deployed using Streamlit.

## Files

1)  `deploy.py` is the file containing streamlit application
2)  `Hotel Reservations.csv` is the dataset used to train the model
3)  `reservation_status_classifier.ipynb` contains data preprocessing and model training code.
4) `model.pkl` contains pickled model
5) `label_decoder.pkl` contains the label decoder (to decode LabelEncoded result). It is the pickled LabelEncoder fit on the data during preprocessing.
6) `column_preprocessor.pkl` is the pickled preprocessor used to (as the name suggests) preprocess the columns of the entered data before being passed to the model for prediction

## Requirements
- **Ipykernel** 
- **Sci-kit Learn**
- **Pandas**
- **XGBoost**
- **Streamlit**

import streamlit as st
import pickle
import pandas as pd

with open("model.pkl", 'rb') as file:
    model = pickle.load(file)

with open("label_decoder.pkl", 'rb') as file:
    decoder = pickle.load(file)

with open("column_preprocessor.pkl", 'rb') as file:
    preprocessor = pickle.load(file)

st.title("Room Cancellation Prediction")

no_of_adults = st.selectbox('Number of Adults', [0, 1, 2, 3, 4])
no_of_children = st.selectbox('Number of Children', [0, 1, 2, 3])
no_of_weekend_nights = st.number_input("Number of Weekend Nights", min_value=0, max_value=10)
no_of_week_nights = st.number_input("Number of Week Nights", min_value=0, max_value=20)
type_of_meal_plan = st.selectbox('Meal Plan', ["Not Selected", "Meal Plan 1", "Meal Plan 2", "Meal Plan 3"])
required_car_parking_space = st.selectbox('Parking Spaces', [0, 1])
room_type_reserved = st.selectbox('Room Type Reserved', ["Room_Type 1", "Room_Type 2r", "Room_Type 3", "Room_Type 4", "Room_Type 5", "Room_Type 6", "Room_Type 7"])
lead_time = st.number_input("Lead_time", min_value=0, max_value=400)
arrival_month = st.number_input("Arrival Month", min_value=1, max_value=12)
market_segment_type = st.selectbox("Market Segment", ["Online", "Offline", "Corporate", "Complementary", "Aviation"])
repeated_guest = st.checkbox("Repeated Guest")
no_of_previous_cancellations = st.number_input("Number of Previous Cancellations", min_value=0, max_value=20)
no_of_previous_bookings_not_canceled = st.number_input("Number of Previous Bookings Not Cancelled", min_value=0, max_value=100)
avg_price_per_room  = st.number_input("Average price / Room", min_value=0.0, max_value=100.0, step=0.1)
number_of_special_requests = st.number_input("Number of Special Requests", min_value=0, max_value=10)

if st.button("Predict"):
    if repeated_guest:
        repeated_guest = 1
    else:
        repeated_guest = 0
    
    data = {
        "no_of_adults" : no_of_adults,
        "no_of_children" : no_of_children,
        "no_of_weekend_nights" : no_of_weekend_nights,
        "no_of_week_nights" : no_of_week_nights,
        "type_of_meal_plan" : type_of_meal_plan,
        "required_car_parking_space" : required_car_parking_space,
        "room_type_reserved" : room_type_reserved,
        "lead_time" : lead_time,
        "arrival_year" : str(2018),
        "arrival_month" : str(arrival_month),
        "market_segment_type" : market_segment_type,
        "repeated_guest" : repeated_guest,
        "no_of_previous_cancellations" : no_of_previous_cancellations,
        "no_of_previous_bookings_not_canceled" : no_of_previous_bookings_not_canceled,
        "avg_price_per_room" : avg_price_per_room,
        "no_of_special_requests" : number_of_special_requests,
    }

    df = pd.DataFrame(data, index=[0])

    preprocessed = preprocessor.transform(df)
    prediction = model.predict(preprocessed)
    decoded_label = decoder.inverse_transform([prediction])

    st.write(f"Booking Cancellation Prediction: {decoded_label[0]}")
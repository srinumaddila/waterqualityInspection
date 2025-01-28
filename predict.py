"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    aluminium = st.slider("Aluminium concentration", float(df["aluminium"].min()), float(df["aluminium"].max()))
    ammonia = st.slider("Ammonia concentration", float(df["ammonia"].min()), float(df["ammonia"].max()))
    arsenic = st.slider("Arsenic concentration", float(df["arsenic"].min()), float(df["arsenic"].max()))
    barium = st.slider("Barium concentration", float(df["barium"].min()), float(df["barium"].max()))
    cadmium = st.slider("Cadmium concentration", float(df["cadmium"].min()), float(df["cadmium"].max()))
    chloramine = st.slider("Chloramine concentration", float(df["chloramine"].min()), float(df["chloramine"].max()))
    chromium = st.slider("Chromium concentration", float(df["chromium"].min()), float(df["chromium"].max()))
    copper = st.slider("Copper concentration", float(df["copper"].min()), float(df["copper"].max()))
    flouride = st.slider("Flouride concentration", float(df["flouride"].min()), float(df["flouride"].max()))
    bacteria = st.slider("Bacteria concentration", float(df["bacteria"].min()), float(df["bacteria"].max()))
    viruses = st.slider("Viruses concentration", float(df["viruses"].min()), float(df["viruses"].max()))
    lead = st.slider("Lead concentration", float(df["lead"].min()), float(df["lead"].max()))
    nitrates = st.slider("Nitrates concentration", float(df["nitrates"].min()), float(df["nitrates"].max()))
    nitrites = st.slider("Nitrites concentration", float(df["nitrites"].min()), float(df["nitrites"].max()))
    mercury = st.slider("Mercury concentration", float(df["mercury"].min()), float(df["mercury"].max()))
    radium = st.slider("Radium concentration", float(df["radium"].min()), float(df["radium"].max()))
    selenium = st.slider("Selenium concentration", float(df["selenium"].min()), float(df["selenium"].max()))
    silver = st.slider("Silver concentration", float(df["silver"].min()), float(df["silver"].max()))
    uranium = st.slider("Uranium concentration", float(df["uranium"].min()), float(df["uranium"].max()))
    
    

    # Create a list to store all the features
    features = [aluminium,ammonia,arsenic,barium,cadmium,chloramine,chromium,copper,flouride,bacteria,viruses,lead,nitrates,nitrites,mercury,radium,selenium,silver,uranium]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Predicted Sucessfully")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The water is not safe for drinking")
        else:
            st.success("The water is safe for drinking")

        # Print the score of the model  
        st.write("The model used is trusted by quality inspectors and has an accuracy of {:.2f} " .format(score*100),"%")

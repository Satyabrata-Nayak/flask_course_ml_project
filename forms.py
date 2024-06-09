from flask_wtf import  FlaskForm
import pandas as pd
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired

X_train=pd.read_csv("data/train.csv").drop(columns=["price"])
X_val=pd.read_csv("data/val.csv").drop(columns=["price"])
X_data= pd.concat([X_train,X_val],axis=0)

class InputForm(FlaskForm):

    airline=SelectField(
        label="Airline",
        choices=X_data.airline.unique(),
        validators=[DataRequired()]
    )

    date_of_journey=DateField(
        label="date of journey".title(),
        validators=[DataRequired()]
    )

    source=SelectField(
        label="source".title(),
        choices=X_data.source.unique(),
        validators=[DataRequired()]
    )
    destination=SelectField(
        label="destination".title(),
        choices=X_data.destination.unique(),
        validators=[DataRequired()]
    )

    dep_time=TimeField(
        label="dep time".title(),
        validators=[DataRequired()]
    )
    
    arrival_time=TimeField(
        label="arrival time ".title(),
        validators=[DataRequired()]
    )

    duration=IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )
    total_stops=IntegerField(
        label="total stops".title(),
        validators=[DataRequired()]
    )
    additional_info	=SelectField(
        label="additional info".title(),
        choices=X_data.additional_info.unique(),
        validators=[DataRequired()]
    )

    submit=SubmitField(label="Predict")
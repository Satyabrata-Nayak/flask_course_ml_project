from flask import (
    Flask,
    render_template,
    url_for,
)
import joblib
import pandas as pd
from forms import InputForm

app=Flask(__name__)
app.config["SECRET_KEY"]="secret_key"

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html",title="Home")
@app.route('/predict',methods=["GET","POST"])
def predict():
    form=InputForm()
    if form.validate_on_submit():

        user_data= pd.DataFrame.from_dict(dict(
            airline=[form.airline.data],
            date_of_journey=[form.date_of_journey.data.strftime("%Y-%m-%d")],
            source=[form.source.data],
            destination=[form.destination.data],
            dep_time=[form.dep_time.data.strftime("%H:%M:%S")],
            arrival_time=[form.arrival_time.data.strftime("%H:%M:%S")],
            duration=[form.duration.data],
            total_stops=[form.total_stops.data],
            additional_info=[form.additional_info.data],
        ))

        model=joblib.load("model.joblib")
        prediction=model.predict(user_data)[0]
        message=f"The expected price of your Flight is {int(prediction)}"

    else:
        message= "Enter Valid inputs to get the predictions!"
    
    return render_template("predict.html",title="Predict",form=form,msg=message)
if __name__=="__main__":
    app.run(debug=True)

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('randomforest.pickle', 'rb'))
#model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    
    res='Normal'
    if output==0:
        res='Insufficient_Weight'
    elif output==2:
        res='Overweight_Level_I'
    elif output==3:
        res='Overweight_Level_II'  
    elif output==4:
        res='Obesity_Type_I'
    elif output==5:
        res='Obesity_Type_II'
    elif output==6:
        res='Obesity_Type_III'   
    

    return render_template('index.html', prediction_text=f'Type of obesity : {res}')


if __name__ == "__main__":
    app.run(debug=False)
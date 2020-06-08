from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np


app = Flask(__name__)

# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 4) 
    loaded_model = pickle.load(open("survive.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 
  
@app.route('/result', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(int, to_predict_list)) 
        result = ValuePredictor(to_predict_list)         
        if int(result)== 1: 
            prediction ='Play'
        else: 
            prediction ='Dont play'            
        return render_template("result.html", prediction = prediction) 




if __name__ == '__main__':
    app.run(debug=True)


# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 17:00:52 2022

@author: Dell
"""

import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
classifier = pickle.load(open('KNN_Deployment.pkl','rb')) 


@app.route('/')
def home():
  
    return render_template("index7.html")
  
@app.route('/predict',methods=['GET'])

def predict():
    
    '''
    For rendering results on HTML GUI
    '''
    Age = int(request.args.get('Age'))
    SibSp = int(request.args.get('SibSp'))
    Parch = int(request.args.get('Parch'))
    Fare = int(request.args.get('Fare'))
    Sex = int(request.args.get('Sex'))
    Pclass = int(request.args.get('Pclass'))
    


    
    prediction = classifier.predict([[Age,  SibSp,  Parch,     Fare, Sex,  Pclass]])
    
        
    return render_template('index7.html', prediction_text='Survival prediction for given condition is : {}'.format(prediction))

if  predict==0:
    print("No chance of survival")
else:
    print("There are chances of survival")
if __name__ == "__main__":
    app.run(debug=True)

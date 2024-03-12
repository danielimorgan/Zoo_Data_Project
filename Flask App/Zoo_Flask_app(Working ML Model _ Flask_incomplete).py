from flask import Flask, render_template, request
from pymongo import MongoClient
import pandas as pd
import joblib
from pycaret.classification import setup, predict_model
import numpy as np


    #This function prompts the user for input and converts the input to boolean values.
    #It returns a dictionary with the user input.
    # Prompt the user for input and convert to boolean values
def get_user_input():
    animal_name = input("Enter the animal name: ")
    hair = input("Does it have hair? (yes/no): ")
    feathers = input("Does it have feathers? (yes/no): ")
    eggs = input("Does it lay eggs? (yes/no): ")
    milk = input("Does it produce milk? (yes/no): ")
    airborne = input("Is it airborne? (yes/no): ")
    aquatic = input("Is it aquatic? (yes/no): ")
    predator = input("Is it a predator? (yes/no): ")
    toothed = input("Does it have teeth? (yes/no): ")
    backbone = input("Does it have a backbone? (yes/no): ")
    air_breather = input("Is it an air breather? (yes/no): ")
    water_breather = input("Is it a water breather? (yes/no): ")
    venomous = input("Is it venomous? (yes/no): ")
    fins = input("Does it have fins? (yes/no): ")
    tail = input("Does it have a tail? (yes/no): ")
    legs = input("How many legs does it have? (Enter a number): ")

    # Convert user input to boolean values
    return {
        "animal_name": animal_name,
        "hair": hair.lower() == 'yes',  # Convert 'yes' to True, 'no' to False
        "feathers": feathers.lower() == 'yes',
        "eggs": eggs.lower() == 'yes',
        "milk": milk.lower() == 'yes',
        "airborne": airborne.lower() == 'yes',
        "aquatic": aquatic.lower() == 'yes',
        "predator": predator.lower() == 'yes',
        "toothed": toothed.lower() == 'yes',
        "backbone": backbone.lower() == 'yes',
        "air_breather": air_breather.lower() == 'yes',
        "water_breather": water_breather.lower() == 'yes',
        "venomous": venomous.lower() == 'yes',
        "fins": fins.lower() == 'yes',
        "tail": tail.lower() == 'yes',
        "legs": int(legs)
    }

# Get user input
animal_data = get_user_input()

input_data = []
input_data.append(animal_data)

animal_input = pd.DataFrame(input_data)

# Load the trained model
tuned_et_model = joblib.load(r'C:\Users\macks\OneDrive\Documents\Project 4\Test 1\tuned_svm_model.pkl')

# Make predictions using the trained model
predictions = predict_model(tuned_et_model, data=animal_input)
print(predictions)

#start the Flask app
app = Flask(__name__)

##This function handles the form submission from the user.
    #It retrieves the form data, creates a dictionary with the data,
    #and renders the success.html template with the animal_data.
    # Get form data from request
@app.route('/submit', methods=['POST'])
def submit():
    animal_name = request.form['animal_name']
    hair = request.form['hair']
    feathers = request.form['feathers']
    eggs = request.form['eggs']
    milk = request.form['milk']
    airborne = request.form['airborne']
    aquatic = request.form['aquatic']
    predator = request.form['predator']
    toothed = request.form['toothed']
    backbone = request.form['backbone']
    air_breather = request.form['air_breather']
    water_breather = request.form['water_breather']
    venomous = request.form['venomous']
    fins = request.form['fins']
    tail = request.form['tail']
    legs = request.form['legs']

    # Create a dictionary with the form data
    animal_data = {
        "animal_name": animal_name,
        "hair": hair,
        "feathers": feathers,
        "eggs": eggs,
        "milk": milk,
        "airborne": airborne,
        "aquatic": aquatic,
        "predator": predator,
        "toothed": toothed,
        "backbone": backbone,
        "air_breather": air_breather,
        "water_breather": water_breather,
        "venomous": venomous,
        "fins": fins,
        "tail": tail,
        "legs": legs
    }

    # Render the success.html template with the animal_data
    return render_template('success.html', animal_data=animal_data)

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)

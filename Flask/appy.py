from flask import Flask, render_template, request
import pandas as pd
import joblib
import sys,json
import sklearn
import logging

# Out all requests and results into a log file
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
#sys.exit()

#load model
model =joblib.load('Models/dt_model.joblib')

#start the Flask app
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

##This function handles the form submission from the user.
    # Get form data from request
@app.route('/submit', methods=['POST'])
def submit():
    print('======>',request.form)
    animal_name = request.form['animal_name']
    hair = request.form.get('hair',0)
    feathers = request.form.get('feathers',0)
    eggs = request.form.get('eggs',0)
    milk = request.form.get('milk',0)
    airborne = request.form.get('airborne',0)
    aquatic = request.form.get('aquatic',0)
    predator = request.form.get('predator',0)
    toothed = request.form.get('toothed',0)
    backbone = request.form.get('backbone',0)
    air_breather = request.form.get('air_breather',0)
    water_breather = request.form.get('water_breather',0)
    venomous = request.form.get('venomous',0)
    fins = request.form.get('fins',0)
    tail = request.form.get('tail',0)
    legs = request.form.get('legs',0)

    # Create a dictionary with the form data
    animal_data = {
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
    print(animal_data)


    animal_input = pd.DataFrame([animal_data])

    # Make predictions using the trained model
    pred = model.predict(animal_input)
    
    
    #print prediction in a list
    k= json.dumps(pred.tolist())
    msg="animal_name: "+ animal_name+", "+ json.dumps(animal_data)+" ==> "+json.dumps(pred.tolist())
    print('msg:',msg)
    # print prediction
    app.logger.info(msg)
    print('result',k)
    return k
    

if __name__ == '__main__':
    # Run the Flask app without debug mode
    app.run(debug=False)


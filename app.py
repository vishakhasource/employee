from flask import Flask,request,jsonify
import numpy as np
import pickle


model = pickle.load(open('empmodel.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    
    department = request.form.get('department')
    region = request.form.get('region')
    education = request.form.get('education')
    gender = request.form.get('gender')
   
    

    input_query = np.array([[department,region,education,gender]])

    result = model.predict(input_query)[0]

    return jsonify({'is_promoted':str(result)})

    #result = {'cgpa': cgpa, 'iq':iq, 'profile_score':profile_score}
    #return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
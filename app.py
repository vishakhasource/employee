from flask import Flask,request,jsonify
import numpy as np
import pickle


# model = pickle.load(open('empmodel.pkl','rb'))

app = Flask(__name__)



@app.route('/')
def helloworld();
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)

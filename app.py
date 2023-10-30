import pickle
from flask import Flask, request, app, jsonify,url_for,render_template
import numPy as np 
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
regmodel = pickle.load(open('regmodel.pkl','rb'))

import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import Flask


app = Flask(__name__)
run_with_ngrok(app)

d = pd.read_excel("planilha.xlsx")


@app.route("/")
def home():
    return ("<marquee><h3> ADD '/input' TO THE URL TO SEE DATA "
            "AND TO SEE FORMATTED DATA PUT ADD '/output' TO THE URL.</h3></marquee>")


@app.route("/input")
def input_page():
    return d.head(6).to_dict()


@app.route('/output', methods=['GET', 'POST'])
def prediction_json():
    return d.head(6).to_html()


app.run()

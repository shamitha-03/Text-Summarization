#  pip install flask

# pip install transformers

from flask import Flask, render_template, request, redirect, url_for,jsonify
from transformers import pipeline

# using pipeline API for summarization task
summarization = pipeline("summarization",model="facebook/bart-large-cnn",use_fast=False,)
#It will download around 1.7GB on first run

def summarize(original_text):
    return summarization(original_text)[0]['summary_text']

# import systemcheck

app = Flask(__name__)

data = "text"
@app.route('/', methods=['GET', 'POST'])
def home():
    global data
    if request.method == 'POST':
        data = request.get_json()
        # print("data",data,type(data),data["text"])
        return jsonify(dict(msg="success"))
    return render_template('home.html')

@app.route('/result/', methods=['GET'])
def results():
    global data
    print("*"*20,"\n",data["text"],"\n","*"*20)
    result = summarize(data["text"][0])
    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run()
    









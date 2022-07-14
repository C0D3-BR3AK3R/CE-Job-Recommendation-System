from msilib.schema import tables
from pydoc import classname
from flask import Flask, render_template, url_for, request
from scripts import JobWebscraper as JWS
from time import sleep
import pandas as pd

df = pd.read_csv('FlaskApp\data\jobs_data.csv')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    skill1 = request.form['skill_1']
    skill2 = request.form['skill_2']
    skill3 = request.form['skill_3']
    skill4 = request.form['skill_4']
    skills = [skill1, skill2, skill3, skill4]
    
    js = JWS.JobScraper()
    js.webscrape_jobs(skills)
    return html_table()

@app.route('/', methods=['POST', 'GET'])
def html_table():
    return render_template('html_table.html', tables=[df.to_html(classes='fl-table', header='true')])


if __name__ == '__main__':
    app.run(debug=True)
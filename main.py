import requests
from flask import Flask, render_template

def get_gender(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    return response.json()["gender"]

def get_age(name):
    response = requests.get(url=f'https://api.agify.io?name={name}')
    return response.json()["age"]

app = Flask(__name__)

@app.route('/guess/<string:name>')
def home(name=None):
    person = {
        'name' : name,
        'gender' : get_gender(name),
        'age' : get_age(name)
    }
    print(person)
    return render_template(template_name_or_list='guess.html', person = person)

if __name__ == '__main__':
    app.run(debug=True)
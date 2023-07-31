# Flask Web App :)
# HTML Tutorial -> https://www.w3schools.com/html/
# Bootstrap tutorial -> https://www.w3schools.com/bootstrap5/index.php/index.php

from flask import *
import datetime
from Session18B import MongoDBHelper

web_app = Flask("Vets App")


@web_app.route("/")
def index():
    # return "This is Amazing. Its: {}".format(datetime.datetime.today())
    return render_template('index.html')


@web_app.route("/register")
def register():
    return render_template('register.html')


@web_app.route("/save-vet", methods=['POST'])
def save_vet():

    vet_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': request.form['pswd'],
        'createdOn': datetime.datetime.today()
    }

    print(vet_data)
    db = MongoDBHelper(collection="vets")
    db.insert(vet_data)

    return "Thank You..."


def main():
    web_app.run()


if __name__ == "__main__":
    main()


# Flask Web App :)
# HTML Tutorial -> https://www.w3schools.com/html/
# Bootstrap tutorial -> https://www.w3schools.com/bootstrap5/index.php/index.php

from flask import *
import datetime
from Session18B import MongoDBHelper
import hashlib

web_app = Flask("Vets App")


@web_app.route("/")
def index():
    # return "This is Amazing. Its: {}".format(datetime.datetime.today())
    return render_template('index.html')


@web_app.route("/register")
def register():
    return render_template('register.html')


@web_app.route("/register-vet", methods=['POST'])
def register_vet():

    vet_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
        'createdOn': datetime.datetime.today()
    }

    print(vet_data)
    db = MongoDBHelper(collection="vets")
    db.insert(vet_data)

    return render_template('home.html')


@web_app.route("/login-vet", methods=['POST'])
def login_vet():

    vet_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
    }

    print(vet_data)
    db = MongoDBHelper(collection="vets")
    documents = list(db.fetch(vet_data))
    print(documents, type(documents))
    if len(documents) == 1:
        return render_template('home.html')
    else:
        return render_template('error.html')


def main():
    web_app.run()


if __name__ == "__main__":
    main()


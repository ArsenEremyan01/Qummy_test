import json
import requests
from test_app import url_get, url_post, username, password, url_send
from test_app.models import Qummy, db
from flask import Blueprint, render_template, flash, url_for, redirect, request

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def index():
    data = Qummy.query.all()
    return render_template("index.html", data=data)


@views.route('/api/', methods=['GET', 'POST'])
def get_data():
    try:
        get_enc_data = requests.get(url_get).text
        encrypted = [i[1:-1] for i in get_enc_data[1:len(get_enc_data) - 1].split(",")]
        deciphered = []
        item = 0
        while item != len(encrypted):
            get_dec_data = requests.post(url_post, auth=(username, password),
                                         json=[encrypted[item]]).text
            deciphered.append(get_dec_data[1:-1])
            item += 1

        adding_to_db(encrypted, deciphered)
    except:
        flash("Повторите попытку")
    return redirect(url_for('views.index'))


def adding_to_db(encrypted, deciphered):
    i = j = 0
    try:
        while i < len(encrypted):
            my_data = Qummy(encrypted_text=encrypted[i], decrypted_text=deciphered[j])
            db.session.add(my_data)
            db.session.commit()
            i += 1
            j += 1
    except:
        flash("Запись дубликатов предотвращён!")


@views.route('/api_send/', methods=['POST'])
def send_to_github():
    try:
        name = request.form['name']
        repo_url = request.form['repo_url']
        dec_data = [str(item.decrypted_text[1:-1]) for item in Qummy.query.all()]
        data = json.dumps({"name": name, "repo_url": repo_url, "result": dec_data},
                          sort_keys=False, indent=4, ensure_ascii=False)
        requests.post(url_send, json=data)
    except:
        flash("Данные не отправлены")
    return redirect(url_for('views.index'))

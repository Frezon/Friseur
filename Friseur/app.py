from flask import Flask, render_template, json, request, redirect, session, url_for
from flaskext.mail import Mail, Message
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from array import *

mysql = MySQL()
mail = Mail()
app = Flask(__name__)
app.secret_key = 'secret'


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''
mysql.init_app(app)


# Mail configurations
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = '25'
app.config['MAIL_USE_TLS'] = 'false'
app.config['MAIL_USE_SSL'] = 'false'
app.config['MAIL_DEBUG'] = 'app.debug'  # TODO: need to switch in the end
app.config['MAIL_USERNAME'] = 'None'
app.config['MAIL_PASSWORD'] = 'None'
app.config['DEFAULT_MAIL_SENDER'] = 'None'
mail.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/reservation', methods=['POST', 'GET'])
def reservation():
    try:
        _vorName = request.form['inputVor']
        _nachName = request.form['inputNach']
        _date = request.form['inputDate']
        _note = request.form['inputNote']
        _phone = request.form['inputPhone']
        _mail = request.form['inputMail']

        if _vorName and _nachName and _date and _note and _phone and _mail:

            # mail message
            msg = Message("Hello",
                          sender="termin@giselas-mobiler-friseurdienst.de",
                          recipients=_mail)
            msg.body = _vorName + _nachName + _phone + _mail + _date + _note
            mail.send(msg)

            # connect to mysql
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ")  # TODO: DB INSERT INTO QUERY
            data = cursor.fetchall()

            if len(data) is 0:
                    conn.commit()
                    return json.dumps({'message': 'Reservation created successfully'})
            else:
                    return json.dumps({'error': str(data[0])})
        else:
                return json.dumps({'html': '<span>Bitte geben Sie alle nötigen Daten an</span>'})
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
import os
from mysql.connector import connect, Error

app = Flask(__name__)

@app.route('/')
def hello():

    return "Hello World!"

@app.route('/poop')
def poop():
    #return os.environ['DB_NAME']
    try:
        with connect(
            host=os.environ["DB_HOST"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"],
        ) as connection:
            return str(connection)
    except Error as e:
        return str(e)


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
from flask import Flask, make_response, request, render_template
import os
from src.hola import hello

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('index.html')


@app.route("/info")
def limit_page():
    return render_template('info.html')

@app.route("/hello")
def say():
    return hello()


# configurar lo que va dentro de PORT es súper importante
app.run(host='0.0.0.0',port=os.getenv("PORT", 5000), debug=True)


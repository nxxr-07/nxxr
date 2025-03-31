from flask import Flask, render_template, request, redirect, url_for, flash
from Website.routes import main

app = Flask(__name__, template_folder='Website/templates', static_folder='Website/static')


app.register_blueprint(main)

if __name__ == '__main__':  
    app.run(debug=True)

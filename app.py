from flask import Flask, render_template, request, redirect, url_for, flash
from Website.routes import main
import os

app = Flask(__name__, template_folder='Website/templates', static_folder='Website/static')


app.register_blueprint(main)

if __name__ == '__main__':  
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


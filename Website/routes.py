from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/resume')
def resume():
    return redirect ("https://drive.google.com/file/d/1o5TbsawU-cI3xvSwLDO7v5w1IZIHWpld/view?usp=sharing")

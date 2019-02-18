from flask import Flask
from flask_nav import Nav
from dominate import tags
from flask import url_for, redirect, flash
from flask import render_template, request
from flask_nav import  register_renderer
from flask_nav.elements import Navbar, View, Link, Text, Separator
from flask_nav.renderers import Renderer, SimpleRenderer
from dashApp.app  import app


if __name__ == '__main__':
    app.run(debug=True)


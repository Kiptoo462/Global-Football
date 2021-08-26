from flask import Blueprint, request, render_template,redirect,url_for,abort
from flask_login import login_required, current_user
from . import main
from app import db
from ..models import User
import urllib.request
from ..request import getTestCall, getLeagues, getCountries, getTeam, getPlayer
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required


@main.route('/home')
@main.route('/')
def index():
    test_call = getTestCall()
    leagues = getLeagues()
    #countries = getCountries()

    title="Home"

    return render_template('index.html',title=title, test_call=test_call, leagues=leagues)
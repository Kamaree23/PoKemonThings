from flask import Blueprint, render_template, request, redirect, flash, url_for

battle = Blueprint('battle', __name__, template_folder='battle_templates')

@battle.route('/battle')
def battleNow():

    return render_template('battle.html')

@battle.route('/winner')
def winnerfun():

    return render_template('battleresult.html')
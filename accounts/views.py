from flask import abort, render_template, request, redirect, url_for, flash
from flask import Blueprint
from flask_login import (
        current_user,
        login_required,
        login_user,
        logout_user
    )
from accounts.encryptions.aes_encryption import AesEncryption

from accounts.extensions import database as db
from accounts.extensions import encryptionClass as ec
from accounts.models import User, Profile
from accounts.forms import (
        RegisterForm, 
        LoginForm, 
        EditUserProfileForm
    )
from accounts.utils import (
        convert_string_to_key,
        unique_security_token,
        get_unique_filename,
    )

from datetime import datetime, timedelta
import re
import os


"""
This accounts blueprint defines routes and templates related to user management
within our application.
"""
accounts = Blueprint('accounts', __name__, template_folder='templates')

# # function is called before each request
# @accounts.before_request
# def before_request():
        


@accounts.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    form = RegisterForm()

    if current_user.is_authenticated:
        return redirect(url_for('accounts.index'))
    if form.validate_on_submit():
        username = form.data.get('username')
        password = form.data.get('password')

        try:
            user = User(
                username=username,
                password=password
            )
            user.set_password(password)
            user.save()
            return redirect(url_for('accounts.login'))
        except Exception as e:
            flash("Something went wrong", 'error')
            return redirect(url_for('accounts.register'))
        
    return render_template('register.html', form=form)


@accounts.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('accounts.index'))

    if form.validate_on_submit():
        username = form.data.get('username')
        password = form.data.get('password')

        user = User.get_user_by_username(username)

        if not user:
            flash("User account doesn't exists.", 'error')
        elif not user.check_password(password):
            flash("Your password is incorrect. Please try again.", 'error')
        else:
            login_user(user, remember=True, duration=timedelta(days=15))
            flash("You are logged in successfully.", 'success')
            return redirect(url_for('accounts.index'))

        return redirect(url_for('accounts.login'))

    return render_template('login.html', form=form)

@accounts.route('/logout', strict_slashes=False)
@login_required
def logout():
    logout_user()
    flash("You're logout successfully.", 'success')
    return redirect(url_for('accounts.login'))


@accounts.route('/', strict_slashes=False)
@accounts.route('/home', strict_slashes=False)
@login_required
def index():
    profile = Profile.query.filter_by(user_id=current_user.id).first_or_404()
    return render_template('index.html', profile=profile)


@accounts.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def profile():
    form = EditUserProfileForm()

    user = User.query.get_or_404(current_user.id)
    profile = Profile.query.filter_by(user_id=user.id).first_or_404()

    if form.validate_on_submit():
        username = form.data.get('username')
        phone_number = form.data.get('phone_number')
        city = form.data.get('city')
        profile_image = form.data.get('profile_image')
        about = form.data.get('about')

        if username in [user.username for user in User.query.all() if username != current_user.username]:
            flash("Username already exists. Choose another.", 'error')
        else:
            # encrypt the data 
            key= convert_string_to_key(user.username)
            ec = AesEncryption(key= key)
            user.username = username
            profile.bio = about
            profile.phone_number = phone_number
            profile.city = city

            if profile_image and getattr(profile_image, "filename"):
                profile.set_avator(profile_image)
            
            db.session.commit()
            flash("Your profile update successfully.", 'success')
            return redirect(url_for('accounts.index'))

        return redirect(url_for('accounts.profile'))
        
    return render_template('profile.html', form=form, profile=profile)


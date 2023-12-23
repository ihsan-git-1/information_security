from werkzeug.utils import secure_filename
from flask import render_template, redirect, url_for
from flask_mail import Message
from accounts.extensions import mail
import uuid
import secrets
import os

def unique_uid():
    return str(uuid.uuid4())

def unique_security_token():
    return str(secrets.token_hex())

def get_unique_filename(filename=None):
    if not filename:
        return None
        
    filename = secure_filename(filename).split(".")
    return "{}.{}".format(str(uuid.uuid4()), filename[len(filename)-1])

def remove_existing_file(path=None):
    if os.path.isfile(path=path):
        os.remove(path)

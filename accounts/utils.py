import base64
import hashlib
from werkzeug.utils import secure_filename
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


def convert_string_to_key(input_string):
  # Create a SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the bytes of the input string
    hash_object.update(input_string.encode())

    # Get the digest of the hash object
    digest = hash_object.digest()

    # Base64 encode the digest and make it URL-safe
    key = base64.urlsafe_b64encode(digest)

    return key

import base64
import hashlib
import uuid
import secrets
import os

def unique_uid():
    return str(uuid.uuid4())

def unique_security_token():
    return str(secrets.token_hex())

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

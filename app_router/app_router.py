import json

from database.database import add_user_db, edit_user_info_db, login_user_db
from encryptions.aes_encryption import AesEncryption
from utils import convert_string_to_key


def handle_AppRouting(jsonString):
    request = json.loads(jsonString)

    # Extract route and parameters from the request
    route = request["route"]
    parameters = request["parameters"]

    print("Activated Route: " + route)

    if route == "signup":
        response = sign_up_route(parameters)

    elif route == "login":
        response = login_route(parameters)

    elif route == "edit":
        response = edit_route(parameters)

    elif route == "verify":
        response = verify_route(parameters)

    else:
        response = "Invalid Route"

    print(response)
    return response


def sign_up_route(parameters):
    response = add_user_db(
        parameters["username"],
        parameters["city"],
        parameters["phone_number"],
        parameters["password"],
        parameters["user_type"],
    )
    return response


def login_route(parameters):
    user = login_user_db(
        parameters["username"],
        parameters["password"]
    )
    if user:
        return f"Login successful! Welcome, {user[1]}"
    else:
        return "Login failed no account available"


def edit_route(parameters):
    aes = AesEncryption(convert_string_to_key(parameters["username"]))

    city = aes.decrypt(parameters["city"])
    phone_number = aes.decrypt(parameters["phone_number"])

    db_response = edit_user_info_db(
        parameters["username"],
        city,
        phone_number,
    )

    return db_response


def verify_route(parameters):
    return parameters

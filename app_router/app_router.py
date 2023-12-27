import json

from database.database import add_user_db, login_user_db


def handle_AppRouting(jsonString):
    request = json.loads(jsonString)

    # Extract route and parameters from the request
    route = request["route"]
    parameters = request["parameters"]

    print("Activated Route: "+route)

    if route == "signup":
        response =  sign_up_route(parameters)

    elif route == "login":
        response = login_route(parameters)

    else:
        response = "Invalid Route"

    print(response)
    return response


def sign_up_route(parameters):    
    response =  add_user_db(
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


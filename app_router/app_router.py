import json

from database.database import add_user_db


def handle_AppRouting(jsonString):
    request = json.loads(jsonString)

    # Extract route and parameters from the request
    route = request["route"]
    parameters = request["parameters"]

    print("Activated Route: "+route)

    if route == "signup":
        response =  sign_up_route(parameters)
        print(response)

    elif route == "login":
        response = {"message": f"Hello, {parameters.get('name', 'Guest')}!"}

    else:
        response = "Invalid Route"

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



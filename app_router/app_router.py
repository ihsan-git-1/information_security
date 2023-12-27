import json

from database.database import add_user_db


def handle_AppRouting(jsonString):
    print(jsonString)

    json_decoder = json.JSONDecoder()
    request = json_decoder.raw_decode(jsonString)

    print("Request in router"+ request)

    # Extract route and parameters from the request
    route = request["route"]
    parameters = request["parameters"]

    print("App Route"+route)
    print("App parameters"+parameters)

    if route == "signup":
        response =  sign_up_route(parameters)

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



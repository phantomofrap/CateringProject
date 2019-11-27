from models.client_model import Client

def create_client(email, password, client_name):
    # 1) Check if email is in database
    # 2) Create the User Object
    new_client = Client(email, password, client_name)
    # 3) Save to the database
    return new_client.save()


def delete_client(id):
    # Grab user from database
    # Delete the user
    pass

def update_client(id, data):
    # Grab user from database
    # Update user fields with data
    # Commit the changes to the database
    pass

def get_client(id):
    # Grab user from database
    # Return that user to the controller
    pass

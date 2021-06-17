from app.main.models import User
import os.path
import json

path = os.path.join(os.path.dirname(__file__), "database.json")

def save_user(user):
    try:
        with open(path, 'r+') as read_file:
            data = json.load(read_file)
            if data.get(user.username) == None:
                data[user.id] = {'username': user.username, 'mail': user.email, 'pass': user.password}
                read_file.seek(0)
                read_file.write(json.dumps(data))
                read_file.close()
            return False
    except:
        with open(path, 'w', encoding ='utf8') as new_file:
            data = {user.id : {'username': user.username, 'mail': user.email, 'pass': user.password}}
            json.dump(data, new_file)

def get_user_by_id(user_id):
    with open(path, 'r+') as read_file:
        data = json.load(read_file)
        read_file.close()
        # return user_id, data.get(user_id)['username'], data.get(user_id)['mail'], data.get(user_id)['pass']
        return User(user_id, data.get(user_id)['username'], data.get(user_id)['mail'], data.get(user_id)['pass'])

def get_user_by_name(username):
    try:
        with open(path, 'r+') as read_file:
            data = json.load(read_file)
            read_file.close()
            for user_id, values in data.items():
                if values['username'] == username:
                    return get_user_by_id(user_id)
    except:
        return None

def get_users():
    with open(path, 'r+') as read_file:
        data = json.load(read_file)
        read_file.close()
        return data

def id_generator():
    try:
        with open(path, 'r') as read_file:
            data = json.load(read_file)
            return str(int(list(data.keys())[-1]) + 1)
    except:
        return str(1)
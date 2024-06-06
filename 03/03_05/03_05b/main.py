user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None,
    "shouldEmpty": ""
}

def update_preferences(user_pref):
    # result = {}
    # for key, value in user_pref.items():
    #     if value is not None and value != '':
    #         result[key] = value
    # return result
    return { 
            key: value for key, value in user_pref.items() 
            if value is not None and value != '' 
        }


print(update_preferences(user_preferences))

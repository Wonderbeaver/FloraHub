
def check_password(password, check_password):
    if password != check_password:
        return 'passwords mismatch'
    elif len(password) < 8:
        return 'too short password'
    


    



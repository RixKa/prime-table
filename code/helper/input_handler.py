

def prompt_user(retry=False):
    if retry:
        n = raw_input('Error: Please enter a valid number: ')
    else:
        n = raw_input('Please enter a number: ')
    return n


def validate_input(n):
    if str(n).isdigit() and int(n) != 0:
        return True
    elif isinstance( n, ( int, long ) )  and n != 0:
        return True
    else:
        return False

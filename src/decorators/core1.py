
def uppercase(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result.upper()

    return wrapper
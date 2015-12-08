def log_and_run(func):
    print("I just got {}".format(func.__name__))
    return func()


def log_and_return(func):
    print("I just got {}".format(func.__name__))
    return func

def say_hello():
    print('Hello!')

new_func = log_and_run(say_hello)

new_func()

from fastapi import FastAPI

api = FastAPI()

def is_setup():
    pass

def first_time_setup():
    pass

def start():
    pass

if __name__ == "__main__":
    if not is_setup():
        first_time_setup()
    start()
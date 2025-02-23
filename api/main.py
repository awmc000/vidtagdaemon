'''
main.py

February 18th, 2025

vidtagdaemon API - a REST API that downloads song videos
from youtube and tags them as requested.
'''
from contextlib import asynccontextmanager
from fastapi import FastAPI
import os

@asynccontextmanager
async def lifespan(api: FastAPI):
    first_time_setup()
    yield
    # TODO: any teardown work

api = FastAPI(lifespan=lifespan)

def is_setup():
    # Check if ./working/ exists.
    workingFolder = os.path.join(os.getcwd(), 'working')
    workingFolderCreated = os.path.exists(workingFolder)
    
    # Check if ./downloads/ exists.
    downloadFolder = os.path.join(os.getcwd(), 'downloads')
    downloadFolderCreated = os.path.exists(downloadFolder)
    
    # Check if vidtagdaemon.json exists.
    configFile = os.path.join(os.getcwd(), 'vidtagdaemon.json')
    configFileCreated = os.path.exists(configFile)
    
    return workingFolderCreated and downloadFolderCreated and configFileCreated

def first_time_setup():
    if not is_setup():
        os.makedirs('working')
        os.makedirs('downloads')
        with open('vidtagdaemon.json', 'w+') as f:
            f.write('{}')

def start():
    pass

@api.get('/')
def reply_to_ping():
    return {"Hello, World!": "Goodbye, Mars!"}
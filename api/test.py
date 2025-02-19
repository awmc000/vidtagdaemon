'''
test.py

February 18th, 2025

Unit tests for the vidtagdaemon API.

Requires that an IP address be passed in
as a command line argument.
'''

import unittest
import requests
import subprocess
import sys

apiAddress = None

class TestApiEndpoints(unittest.TestCase):
    
    def test_got_valid_address(self):
        # TODO: Check if apiAddress is a valid IP address.
        self.assertTrue(False)
        
    def test_api_reachable(self):
        # TODO: Check if requests to apiAddress get a response.
        self.assertTrue(apiAddress is not None)
        r = requests.get(apiAddress)
        self.assertEqual(r.status_code, 200)
    
    def test_api_folders_created(self):
        # TODO: Check that the API created its /working and /downloads folders.
        self.assertTrue(False)
    
    def test_download_single(self):
        payload = {
            'url': 'https://www.youtube.com/watch?v=nIeMvg2vSAw',
            'artist': 'Sematary',
            'title': 'HEART SO PURE' 
        }
        self.assertTrue(apiAddress is not None)
        r = requests.get(apiAddress, params=payload)
        # TODO: Parse JSON in r.text
        # TODO: Get fileName from JSON
        # TODO: Check if fileName exists in downloads directory
        self.assertTrue(False)
    
    def test_video_discarded(self):
        payload = {
            'url': 'https://www.youtube.com/watch?v=nIeMvg2vSAw',
            'artist': 'Sematary',
            'title': 'HEART SO PURE' 
        }
        self.assertTrue(apiAddress is not None)
        r = requests.get(apiAddress, params=payload)
        # TODO: Parse JSON in r.text
        # TODO: Get fileName from JSON
        # TODO: Check if fileName exists in downloads directory
        # TODO: Check that there are no video files in the downloads directory whatsoever
        self.assertTrue(False)
    
    def test_download_album(self):
        payload = {
            'url': 'https://www.youtube.com/watch?v=BkFzSaAx4tI',
            'artist': 'Boards of Canada',
            'title': 'In A Beautiful Place Out In The Country',
            'trackTitles': [
                'Kid For Today',
                'Amo Bishop Roden',
                'In A Beautiful Place Out In The Country',
                'Zoetrope'
            ],
            'cuts': [
                '0:00',
                '6:27',
                '12:44',
                '19:50'
            ]
        }
        # TODO: Parse JSON in r.text
        # TODO: Get fileNames (list) from JSON
        # TODO: Check if each fileName exists in the downloads directory
        self.assertTrue(False)

def find_ip(stdoutString):
    '''
    Pulls the IP from the output of a command to start
    the API.
    '''
    return None

if __name__ == "__main__":
    # TODO: Start up local API process, get its IP
    # command: `fastapi dev main.py`
    apiProcess = subprocess.run(['fastapi', 'dev', 'main.py'], 
        capture_output=True)
    print(f'captured stdout: {apiProcess.stdout}')
    print(f'address is {apiAddress}')
    unittest.main()

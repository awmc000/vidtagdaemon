'''
test.py

February 18th, 2025

Unit tests for the vidtagdaemon API.

Requires that an IP address be passed in
as a command line argument.
'''

import json
import unittest
import requests
import re
import os

apiAddress = None

def valid_ip_address(s: str):
    '''
    Returns True if `s` is a valid IPv4 address
    in dot notation, False otherwise.
    '''
    # String does not exist
    if not s:
        return False
    
    # Unaccepted length
    if len(s) not in range(7, 16):
        return False
    
    bytes = s.split('.')
    
    # Does not contain 4 blocks sep. by dots
    if len(bytes) != 4:
        return False
    
    # Contains any char not a digit or a dot
    for c in s:
        if c not in '0123456789.':
            return False
    
    # Contains any leading zeroes or non-numeric chars in a byte
    for b in bytes:
        if b[0] == '0' and len(b) > 1:
            return False
        
        for c in b:
            if c not in '0123456789':
                return False
    
    # Satisfies all conditions
    return True

def find_ip(s):
    '''
    Pulls the IP from the output of a command to start
    the API.
    '''
    ip_pat = re.compile(r'\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d' +
        r'?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\b')
    s = str(s)
    res = ip_pat.search(s)

    if res is None:
        return None

    try:
        return res.group(0)
    except IndexError:
        return None

class TestUtilityFunctions(unittest.TestCase):
    def test_valid_ips_good_ips(self):
        self.assertTrue(valid_ip_address('0.0.0.0'))
        self.assertTrue(valid_ip_address('192.168.0.1'))
    
    def test_valid_ips_bad_ips(self):
        self.assertFalse(valid_ip_address('012.0.6.8'))
        self.assertFalse(valid_ip_address('ba.0f.de.af'))
        
    def test_find_ip_in_text(self):
        textBlock = '''
            [INFO] 2025-02-18 10:34:56 - Starting vidtagdaemon API...
            [INFO] 2025-02-18 10:34:57 - Configuration loaded successfully.
            [INFO] 2025-02-18 10:34:58 - Server listening on IP address 192.168.1.101.
            [INFO] 2025-02-18 10:35:00 - Vidtagdaemon API is now accepting connections.
        '''
        ip = find_ip(str(textBlock))
        self.assertSequenceEqual(ip, '192.168.1.101')
        self.assertTrue(valid_ip_address(ip))

class TestApiEndpoints(unittest.TestCase):
    
    def test_got_valid_address(self):
        self.assertTrue(valid_ip_address(apiIp))
        
    def test_api_reachable(self):
        self.assertTrue(apiAddress is not None)
        r = requests.get(apiAddress)
        self.assertEqual(r.status_code, 200)
    
    def test_api_folders_created(self):
        # Check if ./working/ exists.
        workingFolder = os.path.join(os.getcwd(), 'working')
        workingFolderCreated = os.path.exists(workingFolder)
        self.assertTrue(workingFolderCreated)
        
        # Check if ./downloads/ exists.
        downloadFolder = os.path.join(os.getcwd(), 'downloads')
        downloadFolderCreated = os.path.exists(downloadFolder)
        self.assertTrue(downloadFolderCreated)
        
        # Check if vidtagdaemon.json exists.
        configFile = os.path.join(os.getcwd(), 'vidtagdaemon.json')
        configFileCreated = os.path.exists(configFile)
        self.assertTrue(configFileCreated)
    
    def test_download_single(self):
        payload = {
            'url': 'https://www.youtube.com/watch?v=nIeMvg2vSAw',
            'artist': 'Sematary',
            'title': 'HEART SO PURE' 
        }
        self.assertTrue(apiAddress is not None)
        r = requests.get(apiAddress, params=payload)

        returned = json.loads(r.text)

        self.assertTrue('fileName' in returned)

        fileName = returned['fileName']

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

if __name__ == "__main__":

    # Start the api, capturing output
    apiIp = '127.0.0.1'
    apiPort = '8000'
    apiAddress = 'http://' + apiIp + ':' + apiPort
    unittest.main()

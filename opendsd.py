#!/usr/bin/env python

import requests
import json

class OpenDSD():
    """OpenDSD Python Library"""
    def __init__(self):
        pass

    def getCodeEnforce(self, id):
        url = 'http://opendsd.sandiego.gov/api/codeenforcement/'+id
        headers = {'Accept': 'application/json'}
        #data = ''

        r = requests.get(url, headers=headers)
        #print r.text
        complainObject = json.loads(r.text)
        if('Description' in complainObject):
            print complainObject['Description']
            print "\n"
        else:
            pass

    def getProject(self, id):
        url = 'http://opendsd.sandiego.gov/api/project/'+id
        headers = {'Accept': 'application/json'}
        #data = ''
        r = requests.get(url, headers=headers)
        print r.text

    def getApproval(self, id):
        url = 'http://opendsd.sandiego.gov/api/approval/'+id
        headers = {'Accept': 'application/json'}
        #data = ''
        r = requests.get(url, headers=headers)
        print r.text

    def getInvoice(self, id):
        url = 'http://opendsd.sandiego.gov/api/project/'+id
        headers = {'Accept': 'application/json'}
        #data = ''
        r = requests.get(url, headers=headers)
        print r.text

    def scrapeComplaints(self):
        for id in range(200000, 222222):
            self.getCodeEnforce(str(id))


if __name__ == '__main__':
    dsd = OpenDSD()
    #dsd.getCodeEnforce('122556')
    dsd.scrapeComplaints()

#!/usr/bin/env python

import requests
import json


class OpenDSD():
    """OpenDSD Python Library"""
    def __init__(self):
        pass

    def getCodeEnforce(self, id):
        ''' Get Code Enforcement Complaint by ID '''
        url = 'http://opendsd.sandiego.gov/api/codeenforcement/'+id
        headers = {'Accept': 'application/json'}
        r = requests.get(url, headers=headers)
        complaintObject = json.loads(r.text)
        
        print r.text
        
        if(complaintObject.get('ErrorMessage') is None):
            return None
        else:
            return complaintObject

    def getProject(self, id):
        ''' Get Project by ID '''
        url = 'http://opendsd.sandiego.gov/api/project/'+id
        headers = {'Accept': 'application/json'}

        r = requests.get(url, headers=headers)
        projectObject = json.loads(r.text)
        
        print r.text
        
        if(projectObject.get('ErrorMessage') is None):
            return None
        else:
            return projectObject

    def getApproval(self, id):
        ''' Get Approval by ID '''
        url = 'http://opendsd.sandiego.gov/api/approval/'+id
        headers = {'Accept': 'application/json'}

        r = requests.get(url, headers=headers)
        approvalObject = json.loads(r.text)
        
        print r.text
        
        if(approvalObject.get('ErrorMessage') is None):
            return None
        else:
            return approvalObject

    def getInvoice(self, id):
        ''' Get Invoice by ID '''
        url = 'http://opendsd.sandiego.gov/api/project/'+id
        headers = {'Accept': 'application/json'}
        #data = ''
        r = requests.get(url, headers=headers)
        invoiceObject = json.loads(r.text)

        print r.text

        if(invoiceObject.get('ErrorMessage') is None):
            return None
        else:
            return invoiceObject

    def getComplaintsByGPS(self):
        url = 'http://opendsd.sandiego.gov/api/CeCaseMapSearch/?SouthWestLatitude=32.71879985593221&SouthWestLongitude=-117.16525563507082&NorthEastLatitude=32.74399836325726&NorthEastLongitude=-117.12534436492922'
        headers = {'Accept': 'application/json'}

        r = requests.get(url, headers=headers)
        regionalComplaints = json.loads(r.text)
        print r.text

        if(regionalComplaints.get('ErrorMessage') is None):
            return None
        else:
            return regionalComplaints

    def scrapeComplaints(self):
        for id in range(200000, 222222):
            self.getCodeEnforce(str(id))


if __name__ == '__main__':
    dsd = OpenDSD()
    #dsd.getCodeEnforce('122556')
    #dsd.scrapeComplaints()
    dsd.getComplaintsByGPS()


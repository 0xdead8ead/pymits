#!usr/bin/env python

from imgurpython import ImgurClient


class GraffitiUpload():

    def __init__(self):
        self.clientId = '7ddd8b0de37d9ff'
        self.clientSecret = '33d86331c3cbff6c77287aa29a8a134aa0a35f86'
        self.fileUploadPath = 'images/'     

    def uploadGraffiti(self, filename):
        print 'hello upload'
        client = ImgurClient(self.clientId, self.clientSecret)

        uploadReturn = client.upload_from_path(self.fileUploadPath+filename, config=None, anon=True)
        print uploadReturn
        graffitiUploadLink = uploadReturn.get('link')
        return graffitiUploadLink


if __name__ == '__main__':

    graff = GraffitiUpload()
    link = graff.uploadGraffiti('graffiti_devil.jpg')
    print 'Imgur Link:\t%s' % link

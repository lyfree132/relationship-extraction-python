import os
import requests
import fileinput

# This class implements a wrapper on the Relationship Extraction service


class RelationshipExtractionService:
    url = None

    def __init__(self):
        self.url = "https://gateway.watsonplatform.net/relationship-extraction-beta/api/v1/sire/0"
        self.user = "<username>"
        self.password = "<password>"

    # Calls the Relationship Extraction API
    def extract(self, text):

        # payload to send to the service
        data = {
            'txt': text,
            'sid': 'ie-en-news',  # English News, for Spanish use: ie-es-news
            'rt': 'xml',
        }

        r = requests.post(self.url,
                          auth=(self.user, self.password),
                          headers = {
                              'content-type': 'application/x-www-form-urlencoded'},
                          data=data
                          )
        print("Request sent. Status code: %d, content-type: %s" %
              (r.status_code, r.headers['content-type']))
        if r.status_code != 200:
            print("Result %s" % r.text)
            raise Exception("Error calling the service.")
        return r.text

if __name__ == '__main__':
    # Wrapper for Relationship Extraction service
    # It will print each line from the standard input and output the result
    service = RelationshipExtractionService()
    for line in fileinput.input():
        print service.extract(line)

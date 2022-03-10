import requests
import json
import base64
import sys
import time
from threading import Thread
import datetime


def encoding_string(msg):
    message_bytes = msg.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


username = 'admin'
password = 'admin'
awx_ip = '192.168.99.168'

base64string = encoding_string(f'{username}:{password}')
#print(base64string)

headers = {
    'Authorization': "Basic " + base64string,
    'Content-Type': 'application/json'
}


def run_template(templateid):

    url = 'http://'+ awx_ip + '/api/v2/job_templates/'+ str(templateid) + '/launch/'
    #print(url)

    data = {
        "extra_vars": {
            "target_host": "server2",
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    resp = json.loads(response.text)
    job_id = resp.get('id','')
    print(f'Template ID: {templateid}, Job ID: {job_id}')


def template15():
    print("template-15(10MB) is running at time: " + str(datetime.datetime.now()))
    run_template(15)

def template16():
    print("template-16(20MB) is running at time: " + str(datetime.datetime.now()))
    run_template(16)

def template17():
    print("template-17(30MB) is running at time: " + str(datetime.datetime.now()))
    run_template(17)


if __name__ == '__main__':
    template_15 = Thread(target = template15)
    template_16 = Thread(target = template16)
    template_17 = Thread(target = template17)

    template_15.start()
    template_16.start()
    template_17.start()


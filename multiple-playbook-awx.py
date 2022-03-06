import requests
import json
import base64
import sys
import time
from threading import Thread


def encoding_string(msg):
    message_bytes = msg.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


username = 'admin'
password = 'admin'
awx_ip = '192.168.0.103'
#templateid = sys.argv[1]


base64string = encoding_string(f'{username}:{password}')
print(base64string)

headers = {
    'Authorization': "Basic " + base64string,
    'Content-Type': 'application/json'
}



def run_template(templateid):

    url = 'http://'+ awx_ip + '/api/v2/job_templates/'+ str(templateid) + '/launch/'
    #print(url)

    # data = {
    #     "extra_vars": {
    #         "target_host": "server2",
    #         "file_name": "text.txt",
    #         "source_file": "/home/server2/sharefile/{{ file_name }}",
    #         "dest_file": "/var/lib/awx/projects/{{ inventory_hostname }}/{{ file_name }}"
    #     }
    # }

    response = requests.post(url, headers=headers)
    #print(response.text)


def template9():
    print("template-9 is running at time: " + str(int(time.time())) + " seconds.")
    run_template(9)

def template10():
    print("template-10 is running at time: " + str(int(time.time())) + " seconds.")
    run_template(10)

def template11():
    print("template-11 is running at time: " + str(int(time.time())) + " seconds.")
    run_template(11)


if __name__ == '__main__':
    template_9  = Thread(target = template9)
    template_10 = Thread(target = template10)
    template_11 = Thread(target = template11)

    template_9.start()
    template_10.start()
    template_11.start()


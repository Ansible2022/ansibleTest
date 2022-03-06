import requests
import json
import base64
import sys
import time
from threading import Thread


username = 'admin'
password = 'admin'
awx_ip = '192.168.60.234'


def encoding_string(msg):
    message_bytes = msg.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


base64string = encoding_string(f'{username}:{password}')
print(base64string)


def run_template(target_host, templateid, filename):

    url = f'http://{awx_ip}/api/v2/job_templates/{str(templateid)}/launch/'

    headers = {
        'Authorization': "Basic " + base64string,
        'Content-Type': 'application/json'
    }

    data = {
        "extra_vars":
            {
                "target_host": target_host,
                "file_name": filename,
            }
    }

    response = requests.post(url, headers=headers,
                             data=json.dumps(data), verify=False)
    
    resp = json.loads(response.text)
    job_id = resp.get('id', '')
    print(f'Job id: {job_id}')


def template9():
    print("template-9(10MB.pdf) is running at time: " +
          str(int(time.time())) + " seconds.")
    run_template("server2", 9, "10MB.pdf")


def template10():
    print("template-10(20MB.zip) is running at time: " +
          str(int(time.time())) + " seconds.")
    run_template("server2", 10, "20MB.zip")


def template11():
    print("template-11(40MB.zip) is running at time: " +
          str(int(time.time())) + " seconds.")
    run_template("server2", 11, "40MB.zip")


def main():
    template_9 = Thread(target=template9)
    template_10 = Thread(target=template10)
    template_11 = Thread(target=template11)

    template_9.start()
    template_10.start()
    template_11.start()


if __name__ == '__main__':
    main()

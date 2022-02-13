import configparser
import json
import requests
from lxml import etree

def get_session():
    login_url = 'http://{}:{}/admin/login/?next=/admin/'.format(server_ipaddr, server_port)
    req = requests.Session()
    rsp = req.get(login_url)
    html = etree.HTML(rsp.text)
    token = html.xpath('//*[@id="login-form"]/input[@name="csrfmiddlewaretoken"]/@value')
    # print(token)
    udata = {
        'username': 'it',
        'password': '1234',
        'csrfmiddlewaretoken': token[0]
    }
    rsp = req.post(login_url, data=udata)
    # print(rsp.content)
    return req

# Read config
conf = configparser.ConfigParser()
conf.read('client.cfg')

curl = conf.get('client', 'curl')
pwd = conf.get('client', 'password')
client_ipaddr = conf.get('client', 'ipaddr')
client_port = conf.get('client', 'port')

server_ipaddr = conf.get('server', 'ipaddr')
server_port = conf.get('server', 'port')
api_url = 'http://{}:{}/api/client'.format(server_ipaddr, server_port)

# Get session
req = get_session()
csrftoken = req.cookies['csrftoken']

# Create user
cdata = {
    'curl': curl,
    'passwd': pwd,
    'ipaddr': client_ipaddr,
    'port': client_port
}
header = {'Content-Type':'application/json; charset=utf-8', 'X-CSRFToken': csrftoken}
rsp = req.post(api_url, headers=header, data=json.dumps(cdata))
# print(rdata)
print(rsp.status_code, rsp.content)



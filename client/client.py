import configparser
import csv
import json
import requests
import rsa
from lxml import etree

def encrypt_data(message):
    with open('public.pem', mode='rb') as pf:
        pub = pf.read()
        pub_key = rsa.PublicKey.load_pkcs1(pub)
        return rsa.encrypt(message, pub_key)

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

def get_country(city_code):
    paser = configparser.ConfigParser()
    paser.read('city_codes.csv')
    try:
        country_code = paser.get('cities', city_code)
    except configparser.NoOptionError:
        return ''
    # print(country_code)
    return country_code

# Read config
conf = configparser.ConfigParser()
conf.read('client.cfg')

curl = conf.get('client', 'curl')
pwd = conf.get('client', 'password')
client_ipaddr = conf.get('client', 'ipaddr')
client_port = conf.get('client', 'port')

server_ipaddr = conf.get('server', 'ipaddr')
server_port = conf.get('server', 'port')
api_url = 'http://{}:{}/api/poster'.format(server_ipaddr, server_port)

csv_path = conf.get('csv', 'path')

# Read csv, convert to json
out = ''
with open(csv_path) as rf:
    fcsv = csv.DictReader(rf)
    jdata = []
    for row in fcsv:
        if row['Country'] == '':
            row['Country'] = get_country(row['City'])
        jdata.append(row)
    # out = json.dumps([row for row in fcsv])
    out = json.dumps(jdata)
    # print(out)

# Get session
req = get_session()
csrftoken = req.cookies['csrftoken']

# Send json
rdata = {
    'content': out,
    'reporter': curl
}
# enc_data = encrypt_data(json.dumps(rdata))
header = {'Content-Type':'application/json; charset=utf-8', 'X-CSRFToken': csrftoken}
rsp = req.post(api_url, headers=header, data=json.dumps(rdata))
# print(enc_data)
print(rsp.status_code, rsp.content)



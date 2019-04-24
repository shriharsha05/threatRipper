try:
  import requests
  from urllib.request import urlopen, pathname2url
except ImportError:
  from urllib import pathname2url
  from urllib2 import urlopen

import json
import pprint

api_key = 'at_FdlCgOLdAmhuP67o2x88QaE4mqLvc'

def print_response(txt):
  response_json = txt.json()
  subdomains = response_json['domain_siblings']
  pprint.pprint(subdomains)
  #print('Chain length: ' + str(len(response_json)))

def connected_domains(domain):
  # url = 'https://api.threatintelligenceplatform.com/v1/connectedDomains'\
  #       + '?apiKey=' + pathname2url(api_key)\
  #       + '&domainName=' + pathname2url(domain)
  # Virus Total API
  url = 'https://www.virustotal.com/vtapi/v2/domain/report'
  params = {'apikey': '53021352fb448ae7dba2c67fed247a1724cc84154a830f34164a73e78e13cfa8',
            'domain': domain}
  response = requests.get(url, params=params)
  try:
    print_response(response)
  except Exception as e:
    print(e)
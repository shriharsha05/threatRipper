try:
  from urllib.request import urlopen, pathname2url
except ImportError:
  from urllib import pathname2url
  from urllib2 import urlopen

import pprint
import json

api_key = 'at_FdlCgOLdAmhuP67o2x88QaE4mqLvc'

def print_response(txt):
  response_json = json.loads(txt)
  pprint.pprint(response_json)
  print('Chain length: ' + str(len(response_json)))

def domain_infrastructure_analysis(domain):
  url = 'https://api.threatintelligenceplatform.com/v1/infrastructureAnalysis'\
        + '?apiKey=' + pathname2url(api_key)\
        + '&domainName=' + pathname2url(domain)

  try:
    print_response(urlopen(url).read().decode('utf8'))
  except Exception as e:
    print(e)
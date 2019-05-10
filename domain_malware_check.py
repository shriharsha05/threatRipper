try:
  from urllib.request import urlopen, pathname2url
except ImportError:
  from urllib import pathname2url
  from urllib2 import urlopen

import json
#import pprint
import requests
from pygments import highlight
from pygments.lexers.data import JsonLexer
from pygments.formatters.terminal import TerminalFormatter

api_key = 'at_FdlCgOLdAmhuP67o2x88QaE4mqLvc'

def print_response(txt, resp2):
  print("Threat Intelligence Platform Analysis")
  response_json = json.loads(txt)
  colorful_json = highlight(json.dumps(response_json, indent=4),
                            JsonLexer(), TerminalFormatter())
  print(colorful_json)
  #pprint.pprint(response_json)
  print("\n\n Virus Total Analysis")
  print(highlight(json.dumps(resp2, indent=4),
                  JsonLexer(), TerminalFormatter()))
  #print('Chain length: ' + str(len(response_json)))

def domain_malware_check(domain):
  #ThreatIntellignece Platform API
  url = 'https://api.threatintelligenceplatform.com/v1/malwareCheck'\
        + '?apiKey=' + pathname2url(api_key)\
        + '&domainName=' + pathname2url(domain)
  #VirusTotal API
  url2 = 'https://www.virustotal.com/vtapi/v2/url/report'
  params = {'apikey': '53021352fb448ae7dba2c67fed247a1724cc84154a830f34164a73e78e13cfa8',
            'resource': domain,'allinfo' : True}
  response = requests.get(url2, params=params)

  try:
    print_response(urlopen(url).read().decode('utf8'),response.json())
  except Exception as e:
    print(e)

try:
  from urllib.request import urlopen, pathname2url
except ImportError:
  from urllib import pathname2url
  from urllib2 import urlopen

import json
#import pprint
from pygments import highlight
from pygments.lexers.data import JsonLexer
from pygments.formatters.terminal import TerminalFormatter

api_key = 'at_FdlCgOLdAmhuP67o2x88QaE4mqLvc'

def print_response(txt):
  response_json = json.loads(txt)
  colorful_json = highlight(json.dumps(response_json, indent=4),
                            JsonLexer(), TerminalFormatter())
  print(colorful_json)
  #pprint.pprint(response_json)
  print('Chain length: ' + str(len(response_json)))

def ssl_certificates_chain(domain):
  url = 'https://api.threatintelligenceplatform.com/v1/sslCertificatesChain'\
        + '?apiKey=' + pathname2url(api_key)\
        + '&domainName=' + pathname2url(domain)

  try:
    print_response(urlopen(url).read().decode('utf8'))
  except Exception as e:
    print(e)

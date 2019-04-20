import pyfiglet
import os
#from domain_infrastructure_analysis.py import domain_infrastructure_analysis
from ssl_certificates_chain import ssl_certificates_chain
# from ssl_configuration_analysis.py import ssl_configuration_analysis
# from domain_malware_check.py import domain_malware_check
# from domain_reputation.py import domain_reputation
# from connected_domains.py import connected_domains

def main_banner():
      os.system("clear")
      print(pyfiglet.figlet_format("threatRipper", font="roman"))
      print("   {1} -- Analysis API")
      print("   {2} -- SSL Certificates Chain")
      print("   {3} -- SSL Configuration Analysis") 
      print("   {4} -- Domain Malware Check")
      print("   {5} -- Connected Domains")
      print("   {6} -- Domain Reputation")  
      print("   {99} -- Exit")
      print("\n\n")
      key = input("threatRipper~# ")

def analysis_banner():

def ssl_certificates_banner():
    #ssl_certificates_chain(key)

def ssl_configuration_banner():

def domain_malware_banner():

def domain_reputation_banner():

def domain_infrastructure_banner():

main_banner()

'''
      __author__ = "Shriharsha M"
      __email__ = "shriharsha05@gmail.com"
'''

import pyfiglet
import pprint
from colorama import Fore, Back, Style
import time
import os
from domain_infrastructure_analysis import domain_infrastructure_analysis
from ssl_certificates_chain import ssl_certificates_chain
from ssl_configuration_analysis import ssl_configuration_analysis
from domain_malware_check import domain_malware_check
from domain_reputation import domain_reputation
from connected_domains import connected_domains
import socket


def is_connected():
    try:
        # connect to the host
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def main_banner():
      """ prints main menu, based on user choice calls respective banner menu """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK+ pyfiglet.figlet_format("threat", font="roman"))
      print(Fore.GREEN + pyfiglet.figlet_format("Ripper", font="roman"))
      print(Style.RESET_ALL + Fore.YELLOW)
      print("   {1} -- Domain Malware Check")
      print("   {2} -- Domain Infrastructure Analysis")
      print("   {3} -- Connected Domains")
      print("   {4} -- SSL Certificates Chain")
      print("   {5} -- Domain Reputation")
      print("   {6} -- SSL Configuration Analysis") 
      print("   {7} -- Whois Check")
      print("   {0} -- Update")
      print("   {99} -- Exit\n")
      print(Fore.RED)
      #check for internet connection
      if is_connected():
            pass
      else:
            print("Please connect to internet first!")
            time.sleep(4)
            main_banner()
      key = input("threatRipper~# ")
      print(Style.RESET_ALL)
      if key == "1":
            domain_malware_banner()    
      elif key == "2":
            analysis_banner()       
      elif key == "3":
            connected_domains_banner()     
      elif key == "4":
            ssl_certificates_banner()
      elif key == "5":
            domain_reputation_banner()
      elif key == "6":
            ssl_configuration_banner()
      elif key == "7":
            whois_check_banner()
      elif key == "0":
            try:
                  os.system("git pull origin master")
            except:
                  print("You dont have git installed!\nvisit source to update : https://github.com/shriharsha05/threatRipper")
            time.sleep(3)
            main_banner()
      elif key == "99":
            os.system("rm -rf __pycache__")
            print("Bye Bye ;_;")
      else:
            print("Please choose wisely!")
            time.sleep(2)
            main_banner()

def analysis_banner():
      """ Domain Infrastructure Analysis Banner """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("Domain Analysis", font="banner"))
      print(Style.RESET_ALL)
      print("Enter domain name :")
      print(Fore.RED)
      ip = input("threatRipper~# ")
      print(Style.RESET_ALL)
      domain_infrastructure_analysis(ip)
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Do Another Domain Infrastructure Analysis")
      print("   {Any Other Key} -- Goto Main Menu")
      print(Fore.RED)
      option = input("threatRipper~# ")
      if option == "1":
            analysis_banner()
      else:
            main_banner()

def ssl_certificates_banner():
      """ SSL Certificates Chain Banner """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("SSL Certificates Chain", font="banner"))
      print(Style.RESET_ALL)
      print("Enter domain name :")
      print(Fore.RED)
      ip = input("threatRipper~# ")
      print(Style.RESET_ALL)
      ssl_certificates_chain(ip)
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Check Another SSL Certificates Chain")
      print("   {Any Other Key} -- Goto Main Menu")
      print(Fore.RED)
      option = input("threatRipper~# ")
      print(Style.RESET_ALL)
      if option == "1":
            ssl_certificates_banner()
      else:
            main_banner()

def ssl_configuration_banner():
      """ SSL Configuration Analysis Banner """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("SSL Config Analysis", font="banner"))
      print(Style.RESET_ALL)
      print("Enter domain name :")
      print(Fore.RED)
      ip = input("threatRipper~# ")
      print(Style.RESET_ALL)
      ssl_configuration_analysis(ip)
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Do Another SSL Configuration Analysis")
      print("   {Any Other Key} -- Goto Main Menu")
      print(Fore.RED)
      option = input("threatRipper~# ")
      print(Style.RESET_ALL)
      if option == "1":
            ssl_configuration_banner()
      else:
            main_banner()

def domain_malware_banner():
      """ Domain Malware Check Banner """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("Domain Malware Check", font="banner"))
      print(Style.RESET_ALL)
      print("Enter domain name :")
      print(Fore.RED)
      ip = input("threatRipper~# ")
      print(Style.RESET_ALL)
      domain_malware_check(ip)
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Do Another Domain Malware Check")
      print("   {Any Other Key} -- Goto Main Menu")
      print(Fore.RED)
      option = input("threatRipper~# ")
      print(Style.RESET_ALL)
      if option == "1":
            domain_malware_banner()
      else:
            main_banner()

def domain_reputation_banner():
      """ Domain Reputation Banner """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("Domain Reputation", font="banner"))
      print(Style.RESET_ALL)
      print("Enter domain name :")
      print(Fore.RED)
      ip = input("threatRipper~# ")
      print(Style.RESET_ALL)
      domain_reputation(ip)
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Do Another Domain Reputation Check")
      print("   {Any Other Key} -- Goto Main Menu")
      print(Fore.RED)
      option = input("threatRipper~# ")
      print(Style.RESET_ALL)
      if option == "1":
            domain_reputation_banner()
      else:
            main_banner()

def connected_domains_banner():
      """ Connected Domains Banner """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("Connected Domains", font="banner"))
      print(Style.RESET_ALL)
      print("Enter domain name :")
      print(Fore.RED)
      ip = input("threatRipper~# ")
      print(Style.RESET_ALL)
      connected_domains(ip)
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Do Another Connected Domains Check")
      print("   {Any Other Key} -- Goto Main Menu")
      print(Fore.RED)
      option = input("threatRipper~# ")
      print(Style.RESET_ALL)
      if option == "1":
            connected_domains_banner()
      else:
            main_banner()

def whois_check_banner():
      """ Connected Domains Banner """
      os.system("clear")
      print(Fore.GREEN + Back.BLACK +
            pyfiglet.figlet_format("Whois check", font="banner"))
      print(Style.RESET_ALL)
      print("Enter domain name :")
      print(Fore.RED)
      ip = input("threatRipper~# ")
      print(Style.RESET_ALL)
      pprint.pprint(os.system("whois "+ip))
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Do Another Whois Check")
      print("   {Any Other Key} -- Goto Main Menu")
      print(Fore.RED)
      option = input("threatRipper~# ")
      print(Style.RESET_ALL)
      if option == "1":
            whois_check_banner()
      else:
            main_banner()

if __name__ == "__main__":
      main_banner()

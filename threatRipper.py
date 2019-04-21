'''
      __author__ = "Shriharsha M"
      __email__ = "shriharsha05@gmail.com"
'''

import pyfiglet
from colorama import Fore, Back, Style
import time
import os
from domain_infrastructure_analysis import domain_infrastructure_analysis
from ssl_certificates_chain import ssl_certificates_chain
from ssl_configuration_analysis import ssl_configuration_analysis
from domain_malware_check import domain_malware_check
from domain_reputation import domain_reputation
from connected_domains import connected_domains

def main_banner():
      """ prints main menu, based on user choice calls respective banner menu """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK+ pyfiglet.figlet_format("threat", font="roman"))
      print(Fore.GREEN + pyfiglet.figlet_format("Ripper", font="roman"))
      print(Style.RESET_ALL + Fore.YELLOW)
      print("   {1} -- Domain Infrastructure Analysis")
      print("   {2} -- SSL Certificates Chain")
      print("   {3} -- SSL Configuration Analysis") 
      print("   {4} -- Domain Malware Check")
      print("   {5} -- Connected Domains")
      print("   {6} -- Domain Reputation")  
      print("   {99} -- Exit\n")
      print(Fore.RED)
      key = input("threatRipper~# ")
      print(Style.RESET_ALL)
      if key == "1":
            analysis_banner()
      elif key == "2":
            ssl_certificates_banner()
      elif key == "3":
            ssl_configuration_banner()
      elif key == "4":
            domain_malware_banner()
      elif key == "5":
            connected_domains_banner()
      elif key == "6":
            domain_reputation_banner()
      elif key == "99":
            print("Bye Bye :)")
      else:
            print("Please choose wisely!")
            time.sleep(5)
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
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("SSL Configuration Analysis", font="banner"))
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

main_banner()
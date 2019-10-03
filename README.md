# threatRipper v1.0
*May 12, 2019*

![](https://drive.google.com/uc?id=1ZkT6zUXFLMHQjM7kV6-dOi4zIj8eTbLC)
<br>
threatRipper is a command-line tool for 'web threat intelligence' built using python and powered by 'Virus Total' and 'Threat Intelligence Platform' API's.

# Features

  - **Domain Malware Check**: Check if the domain is considered to be dangerous in 70 antivirus scanners and URL/domain blacklisting services, in addition to a variety of tools to extract signals from the studied content.
  
  - **Domain Infrastructure Analysis**: For a given domain name, get a collection of its web, mail, and name servers as well as its known subdomains. For each infrastructure entry, find out its IP address, geolocation and subnetwork information.
  
  - **Connected Domains Details**: Retrieve a list of domain names resolving to a given IP address, including subdomains. Make sure the website does not share the IP address with malicious domains, as that may result in overblocking – a situation when a blocked malicious site also blocks other sites with the same IP. Research the infrastructure of connected domains.
  
  - **SSL Certificates Chain**: For a given domain name, get detailed information about its SSL Certificate and the complete SSL Certificates chain. The data is provided in a unified and consistent JSON format and could be easily integrated with your system.
  
  - **Domain Reputation Details**: For a given domain name or IPv4 address, collect and evaluate over 120 parameters and calculate the resulting reputation score.
  
  - **SSL Configuration Analysis**: For a given domain name, establish and test SSL connection to the host and analyze how it is configured - to detect common configuration issues potentially leading to vulnerabilities.
  
  - **Whois Check**: Retrieve, output and analyze domain name's WHOIS record.

### Installation

threatRipper requires [Python 3](https://www.python.org/download/releases/3.0/)+ to run.

```sh
Using Python Virtual Environment
$ git clone github.com/shriharsha05/threatRipper.git
$ cd threatRipper/
$ sh install.sh

or

Using Docker Image
$ git clone github.com/shriharsha05/threatRipper.git
$ sudo docker build -t "app" ./threatRipper
$ sudo docker run -i app
```

### Use cases 

- **Threat Intelligence Analysis for Investigators**
Find detailed information about a host and the underlying infrastructure in seconds.

### Known Issues

- SSL Configuration Analysis API doesn't work sometimes.

### Change Log

 - 1.0 Initial Release

### Todos

 - Automatically alert website admin about detected threats through mail
 - Introduce user friendly web interface
 - Integration of other Open Source security tools

**Free Tool, Hell Yeah!**

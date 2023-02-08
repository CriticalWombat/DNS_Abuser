from nslookup import Nslookup
from time import sleep

query = Nslookup(dns_servers=['10.14.9.70'])

with open("alexa-domains.txt") as domains:
    i=0
    for domain in domains:
        i += 1
        domain = domain.strip('\n')
        record = query.dns_lookup(domain)
        print(f'{domain} #{i}')
        sleep(.1)